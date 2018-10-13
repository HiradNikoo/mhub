from googleapiclient.discovery import build
from config import configuration
import pprint

class Google(object):
    def __init__(self):
        self.cx_youtube_search = configuration("google", "cx", "youtube-search")

    def search_youtube(self, q):
        service = build("customsearch", "v1", developerKey=configuration("google", "api_key"))
        res = service.cse().list(q=q, cx=self.cx_youtube_search).execute()
        pprint.pprint(res)
