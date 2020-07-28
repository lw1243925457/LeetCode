"""
28. 实现 strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0
        if m > n:
            return -1

        start = 0
        end = start + m
        while end <= n:
            if haystack[start] == needle[0] and haystack[start:end] == needle:
                return start
            start += 1
            end = start + m

        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr("daw", "") == 0
    assert s.strStr("dw", "dfas") == -1

    haystack = "hello"
    needle = "ll"
    assert s.strStr(haystack, needle) == 2

    haystack = "aaaaa"
    needle = "bba"
    assert s.strStr(haystack, needle) == -1
