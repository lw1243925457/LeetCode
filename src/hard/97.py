"""
97. 交错字符串
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
通过次数18,187提交次数43,543
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (m + 1)] * (n + 1)
        dp[0][0] = True

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                p = i + j - 1
                if i > 0:
                    dp[i][j] &= (dp[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    dp[i][j] |= (dp[i][j - 1] and s2[j - 1] == s3[p])

        return dp[n][m]


if __name__ == "__main__":
    s = Solution()
    assert s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
    assert not s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
