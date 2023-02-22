import os
import requests
from flask import json
from shorty.providers.shortlink_provider import ShortlinkProvider

class Bitly(ShortlinkProvider):
    def __init__(self, url: str):
        self.url = url

    def shortenUrl(self) -> str:
        try:
            payload = {"long_url": self.url}
            headers = {
                'Authorization': 'Bearer '+os.getenv("BITLY_TOKEN"),
                'Content-type': 'application/json'
            }

            response = requests.post(
                os.getenv("BITLY_ENPOINT"), headers=headers, data=json.dumps(payload)
            )
                
            shortenedUrl = response.json()['link']
        except:
            shortenedUrl = ''

        return shortenedUrl