import yaml
class Configuration(object):
    params = {}
    with open("config.yml", 'r') as config_stream:
        try:
            params = yaml.load(config_stream)
        except yaml.YAMLError as exc:
            print(exc)