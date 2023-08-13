import json


class Configuration:
    def __init__(self):
        try:
            # Get the values from config file
            self.configuration = json.load(open("config.json"))
        except FileNotFoundError:
            print("Config file does not exist")

    def polling_time(self):
        return self.configuration["polling_time_seconds"]

    def facility_ids(self):
        return self.configuration["facility_id_list"]
