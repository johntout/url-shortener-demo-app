import os
import requests
from shorty.providers.shortlink_provider import ShortlinkProvider

class TinyUrl(ShortlinkProvider):
    def __init__(self, url: str):
        self.url = url

    def shortenUrl(self) -> str:
        try:
            response = requests.get(os.getenv("TINYURL_ENDPOINT")+'?url='+self.url)
            shortenedUrl = response.text
        except:
            shortenedUrl = ''
        
        return shortenedUrl