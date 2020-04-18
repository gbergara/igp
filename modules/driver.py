import yaml

DRIVER_CONFIGS = "config/drivers.yml"


class Driver():

    def __init__(self, name):
        self.name = name

    def details(self):
        with open(DRIVER_CONFIGS, 'r') as config_file:
            drivers = yaml.safe_load(config_file)
            for driver in drivers:
                if self.name in driver.keys():
                    return driver[self.name]
            return None
