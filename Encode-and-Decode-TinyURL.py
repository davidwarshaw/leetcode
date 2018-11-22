#!/usr/bin/env python

import random

class Codec:

    def __init__(self):
        random.seed(1)
        self.protocol_host = 'http://tinyurl.com/'
        self.urls = {}
        self.chars = []
        self.chars.extend([chr(i) for i in range(49, 58)])
        self.chars.extend([chr(i) for i in range(65, 91)])
        self.chars.extend([chr(i) for i in range(97, 123)])

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = ''.join(random.sample(self.chars, 6))
        self.urls[key] = longUrl
        return self.protocol_host + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.replace(self.protocol_host, '')
        return self.urls[key] if key in self.urls else None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
inputs = [['https://google.com'], ['www.something.somewhere']]

if __name__ == '__main__':
    codec = Codec()
    for input in inputs:
        expected = input
        actual = codec.decode(codec.encode(input))
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
