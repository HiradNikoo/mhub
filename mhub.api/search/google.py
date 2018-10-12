from config import configuration
class Google(object):
    def __init__(self):
        self.api_key = configuration('google_api_key')