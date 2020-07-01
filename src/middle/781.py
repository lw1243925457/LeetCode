"""
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100


解题思路：
两个整数组的长度是否一样，需要考虑不一样的情况
可以从最长的开始找，找到第一个就结束
最差的情况是两个数字中没有一个重复的，那需要返回0

最长的长度最大为两数组中长度较小的
如果其中一个数组为空，则返回0

公共的部分，必定是相连的，设置左右指针，一起移动遍历即可
需要两个数组都遍历，还涉及到比较，最坏时间复杂度就3次方了。。。。。。

暴力的时间复杂度太高了，超过了限制。。。。。。
使用官方动态规划算法
"""
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = []
        for i in range(0, m+1):
            dp.append([])
            for j in range(0, n+1):
                dp[i].append(0)

        result = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
                result = max(result, dp[i][j])
        print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.findLength([1], [2]) == 0
    assert s.findLength([1, 2, 3, 5, 6], [5, 6, 1, 2, 3]) == 3
    assert s.findLength([1, 2, 3, 5, 4], [7, 8, 9, 10, 3]) == 1
