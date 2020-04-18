import yaml

GENERAL_CONFIGS = "config/general.yml"


class Config():

    def api_key(self):
        with open(GENERAL_CONFIGS, 'r') as config_file:
            configs = yaml.safe_load(config_file)
            for config in configs:
                return config['openweathermaps_api_key']
