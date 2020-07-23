"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
通过次数143,793提交次数313,152
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            la = s[l].isalpha() or s[l].isdigit()
            ra = s[r].isalpha() or s[r].isdigit()
            if la and ra:
                if s[l].lower() != s[r].lower():
                    return False
                l = l + 1
                r = r - 1
            elif la and not ra:
                r = r - 1
            elif not la and ra:
                l = l + 1
            elif not la and not ra:
                r = r - 1
                l = l + 1
        return True


if __name__ == "__main__":
    s = Solution()
    # assert s.isPalindrome("A man, a plan, a canal: Panama")
    # assert not s.isPalindrome("race a car")
    # assert not s.isPalindrome("0P")
    assert not s.isPalindrome(",,,,,,,,,,,,acva")
