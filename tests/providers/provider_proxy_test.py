from shorty.providers.provider_proxy import ProviderProxy

class TestProvider:
    def test_callProvider(self):
        url: str = 'https://google.com'
        provider: str = 'Bitly'

        sut = ProviderProxy(url, provider).callProvider()
        assert sut == {'link': 'https://bit.ly/3tWLUSJ', 'url': 'https://google.com'}

    @staticmethod
    def test_errorResponse():
        sut = ProviderProxy.errorResponse()
        assert sut == {'success':False, 'message':'There was an issue while contacting the providers. Please try again later.', 'status': 500}
