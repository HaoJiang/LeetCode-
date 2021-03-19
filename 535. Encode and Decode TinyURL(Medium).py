import base64, string, random


class Codec:
    def __init__(self):
        self.hash_url = {}
        self.prefix_url = 'http://tinyurl.com/'
        self.suffix = string.ascii_letters + string.digits

    def get_key(self):
        ky = self.suffix
        return ''.join(random.sample(ky, 6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        _suffix = self.get_key()
        while _suffix in self.hash_url:
            _suffix = self.get_key()

        self.hash_url[_suffix] = longUrl
        return self.prefix_url + _suffix

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # print(self.hash_url.get(shortUrl.replace(self.prefix_url, ''), None))
        return self.hash_url.get(shortUrl.replace(self.prefix_url, ''), None)


url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
codec.decode(codec.encode(url))
