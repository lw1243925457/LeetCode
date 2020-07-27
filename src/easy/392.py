"""
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢:

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

通过次数56,981提交次数114,563


解题思路：
s 是 t 的子序列：s中的字符才t中存在，且是递增的
首先遍历s，一个指针记录访问到的t的位置p
    当出现s[i],没有在t中找到的情况就返回false
一直遍历完成就返回true

s长度为n，t长度为m，两个都遍历了一遍，时间复杂度O(N+M)

上面的解题思路本质上是题解的双指针
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n == 0:
            return True
        if n > m:
            return False

        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n


if __name__ == "__main__":
    s = Solution()
    assert not s.isSubsequence("234", "2")
    assert s.isSubsequence("234", "223344")
    assert not s.isSubsequence("234", "42233555")
