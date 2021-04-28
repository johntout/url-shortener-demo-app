from shorty.factories.provider import Provider

class TestProvider:
    def test_callProvider(self):
        url: str = 'https://google.com'
        provider: str = 'Bitly'

        sut = Provider(url, provider).callProvider()
        assert sut == {'link': 'https://bit.ly/3tWLUSJ', 'url': 'https://google.com'}

    @staticmethod
    def test_errorResponse():
        sut = Provider.errorResponse()
        assert sut == {'success':False, 'message':'There is an issue while contacting the providers. Please try again later.', 'status': 500}
