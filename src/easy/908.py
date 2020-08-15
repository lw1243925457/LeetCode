"""
908. 最小差值 I
给你一个整数数组 A，请你给数组中的每个元素 A[i] 都加上一个任意数字 x （-K <= x <= K），从而得到一个新数组 B 。

返回数组 B 的最大值和最小值之间可能存在的最小差值。



示例 1：

输入：A = [1], K = 0
输出：0
解释：B = [1]
示例 2：

输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]
示例 3：

输入：A = [1,3,6], K = 3
输出：0
解释：B = [3,3,3] 或 B = [4,4,4]


提示：

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        n = len(A)
        if n < 2:
            return 0

        maxValue, minValue = A[0], A[0]
        for num in A:
            if num > maxValue:
                maxValue = num
            if num < minValue:
                minValue = num

        if maxValue - minValue > 2 * K:
            return (maxValue - K) - (minValue + K)
        else:
            return 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.smallestRangeI(A=[1], K=0) == 0
    assert solution.smallestRangeI(A=[0, 10], K=2) == 6
    assert solution.smallestRangeI(A=[1, 3, 6], K=3) == 0
