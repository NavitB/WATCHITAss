import json
import time
import requests
from sensors import *


class MainService:

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.sensors = {}
        self.read_config()

    def read_config(self):
         with open(self.config_file, 'r') as file:
            self.config = json.load(file)

         for sensor_config in self.config['sensors']:
            sensor_type = sensor_config['type']
            valid_range = sensor_config['valid_range']
            
            if sensor_type == 'TemperatureSensor':
                sensor = TemperatureSensor(sensor_type)
            elif sensor_type == 'HumiditySensor':
                sensor = HumiditySensor(sensor_type)
            elif sensor_type == 'PressureSensor':
                sensor = PressureSensor(sensor_type)
            else:
                print(f"Unknown sensor type: {sensor_type}")
                continue

            self.sensors[sensor_type] = (sensor,valid_range) #self.sensors = {sensor_type: (sensor_obj, valid_range)}

    def validate_data(self, data, valid_range):
        return valid_range[0] <= data <= valid_range[1]

    def send_alert(self, sensor_type, data):
        alert_data = {'sensor': sensor_type, 'data': data}
        requests.post('http://localhost:5000/alert', json=alert_data)

    def start_monitor(self):
        while True:
            for sensor_type ,(sensor, valid_range) in self.sensors.items():
                data = sensor.get_data()
                if not self.validate_data(data, valid_range):
                    self.send_alert(sensor_type, data)

                time.sleep(5)

#run the main service seperatly 
if __name__ == "__main__":
    main_service = MainService()
    main_service.start_monitor()