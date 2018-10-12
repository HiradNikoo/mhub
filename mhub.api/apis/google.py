from vendor.googleapiclient.discovery import build
from config import configuration

class Google(object):
    def __init__(self):
        self.api_key = configuration('google', 'api_key')
        self.cx_youtube = configuration('google', 'cx', 'youtube')

    def search_youtube():
        googleapis.googleapis.GoogleApis.search_youtube
    