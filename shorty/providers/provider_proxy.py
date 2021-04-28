from shorty.providers.bitly import Bitly
from shorty.providers.tinyurl import TinyUrl

class ProviderProxy:
    validProviders: dict = {
        'primaryProvider': 'Bitly',
        'fallBackProvider': 'TinyUrl'
    }

    def __init__(self, url, provider):
        self.url: str = url
        self.provider: str = provider
        
        if len(self.provider) == 0 or self.provider not in self.validProviders.values():
            self.provider = self.validProviders['primaryProvider']

    def callProvider(self) -> dict:
        try:
            providerInstance = globals()[self.provider]
            service = providerInstance(self.url)
            shortenedUrl: str = service.shortenUrl()

            if len(shortenedUrl) == 0:
                if (self.provider == self.validProviders['primaryProvider']):
                    providerInstance = globals()[self.validProviders['fallBackProvider']]
                else:
                    providerInstance = globals()[self.validProviders['primaryProvider']]

                service = providerInstance(self.url)
                shortenedUrl = service.shortenUrl()
        except:
            return self.errorResponse()

        if len(shortenedUrl) == 0:
            return self.errorResponse()

        return {'url':self.url, 'link':shortenedUrl}

    @staticmethod
    def errorResponse() -> dict:
        return {'success':False, 'message':'There was an issue while contacting the providers. Please try again later.', 'status': 500}