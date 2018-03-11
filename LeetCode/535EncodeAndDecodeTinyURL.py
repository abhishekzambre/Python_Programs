import uuid

class Codec:

    urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        hash = uuid.uuid4().hex

        self.urls[hash] = longUrl

        return "http://tinyurl.com/" + hash

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls.get(shortUrl[19:], "")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

obj = Codec()

shorturl = obj.encode("www.google.com")
print(shorturl)
print(obj.decode(shorturl))