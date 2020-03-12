"""
535. TinyURL 的加密与解密
TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
"""


class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        result = ""
        for i in range(8, len(longUrl)):
            result = result + chr(ord(longUrl[i]) - 1)
        return result

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        result = ""
        for i in range(7, len(shortUrl)):
            result = result + chr(ord(shortUrl[i]) + 1)
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
if __name__ == "__main__":
    url = "https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    encodeStr = codec.encode(url)
    decodeStr = codec.decode(encodeStr)
    print(encodeStr)
    print(decodeStr)
