"""
409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
通过次数20,105提交次数38,042
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 1:
            return 0

        if len(s) == 1:
            return 1

        statistic = {}
        for c in s:
            if c in statistic:
                statistic[c] = statistic[c] + 1
            else:
                statistic[c] = 1

        amount = len(s)
        result = 0
        for cs in statistic:
            if statistic[cs] >= 2:
                if statistic[cs] % 2 == 0:
                    result = result + statistic[cs] / 2
                    amount = amount - statistic[cs]
                else:
                    result = result + int(statistic[cs] / 2)
                    amount = amount - statistic[cs] + 1

        result = int(result) * 2
        if amount > 0:
            result = result + 1

        # print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("abccccdd") == 7
