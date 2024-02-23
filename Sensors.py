from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def read_data(self):
        pass


class TemperatureSensor(Sensor):

    def __init__(seslf, type):
        super.__init__(type)

    def read_data(self):
        return random.uniform(-20, 180) #in celsius
    

class HumiditySensor(Sensor):

    def __init__(seslf, type):
        super.__init__(type)

    def read_data(self):
        return random.uniform(-20, 180)
     

class PressureSensor(Sensor):

    def __init__(seslf, type):
        super.__init__(type)

    def read_data(self):
        return random.uniform(0, 1500)
     
   

