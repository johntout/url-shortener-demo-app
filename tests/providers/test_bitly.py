from shorty.providers.bitly import Bitly

class TestBitly:
    def test_shortenUrl(self):
        url: str = 'https://google.com'
        assert Bitly(url).shortenUrl() == 'https://bit.ly/3tWLUSJ'
        
