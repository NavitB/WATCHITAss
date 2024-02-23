import json

class MainService:

    def __init__(self, config_file):
        self.config_file = config_file

    def read_config(self):
         with open(self.config_file, 'r') as file:
            self.config = json.load(file)

    def check_valid_data(self, data, valid_range):
        return valid_range[0] <= data <= valid_range[1]

    def start(self):
        self.read_config()
        print(self.config)
