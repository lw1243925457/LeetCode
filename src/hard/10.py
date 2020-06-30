"""
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false


解题思路：
关键点：*能进行两个操作，一个是不匹配字符，一个是匹配字符
使用递归解决
结束条件：s和p字符串最后都为空


感想：
自己水平还是有点菜啊。。。。。。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print(s, p)
        if p == "":
            return s == ""

        # 首先判断字符是否匹配
        firstMatch = len(s) > 0 and p[0] in {s[0], '.'}

        # 处理 * 的情况,注意*必须与其前面的字符一起处理,不匹配或者进行匹配
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))

        # 处理 . 的情况
        return firstMatch and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("aa", "a*")
    assert s.isMatch("", "")
    assert not s.isMatch("", "a")
    assert not s.isMatch("", ".")
    assert not s.isMatch("", ".")
    assert not s.isMatch("aa", "aab")
    assert not s.isMatch("ab", ".*")
    assert not s.isMatch("aa", "a")
    assert s.isMatch("aa", "a*")
    assert s.isMatch("aab", "c*a*b")
    assert not s.isMatch("mississippi", "mis*is*p*.")
    assert not s.isMatch("aaa", "ab*a")
    assert s.isMatch("aaa", "ab*a*c*a")
