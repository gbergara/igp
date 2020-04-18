import yaml
import requests
from modules import config

CIRCUIT_CONFIGS = "config/circuits.yml"
OWM_API_URL = "https://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid={}"


class Circuit():

    def __init__(self, name):
        self.name = name
        configuration = config.Config()
        self.api_key = configuration.api_key()

    def setup_params(self):
        with open(CIRCUIT_CONFIGS, 'r') as config_file:
            circuits = yaml.safe_load(config_file)
            for circuit in circuits:
                if self.name in circuit.keys():
                    return circuit[self.name]
            return None
    def temperature(self):
        params = self.setup_params()
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(params['city_code'], self.api_key))
        return r.json()

