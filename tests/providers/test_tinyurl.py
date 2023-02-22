from shorty.providers.tinyurl import TinyUrl

class TestTinyUrl:
    def test_shortenUrl(self):
        url: str = 'https://google.com'
        assert TinyUrl(url).shortenUrl() == 'https://tinyurl.com/mbq3m'
        
