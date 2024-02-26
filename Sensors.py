from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def get_data(self):
        pass


class TemperatureSensor(Sensor):
    def __init__(self, type):
        super().__init__(type)

    def get_data(self):
        return random.uniform(-50, 200)
    

class HumiditySensor(Sensor):
    def __init__(self, type):
        super().__init__(type)

    def get_data(self):
        return random.uniform(0, 200)
     

class PressureSensor(Sensor):
    def __init__(self, type):
        super().__init__(type)

    def get_data(self):
        return random.uniform(0, 1500)
     
   

