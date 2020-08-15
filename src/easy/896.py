"""
896. 单调数列
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。



示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true


提示：

1 <= A.length <= 50000
-100000 <= A[i] <= 100000


解题思路：
边界条件：
    空和已应该返回true
    全是一样的数，返回true

1.取第一个和最后一个元素，判断其单调方向，遍历判断是否全部单调
"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n < 2:
            return True

        isAdd = (A[0] <= A[-1])
        for i in range(0, n-1):
            if isAdd and A[i] > A[i+1]:
                return False
            elif not isAdd and A[i] < A[i+1]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isMonotonic([])
    assert solution.isMonotonic([1])
    assert solution.isMonotonic([1, 2, 3, 4])
    assert solution.isMonotonic([1, 1, 1, 1])
    assert not solution.isMonotonic([1, 2, 3, 4, 2, 6])
    assert solution.isMonotonic([9, 8, 7, 6, 4, 3])
    assert not solution.isMonotonic([9, 8, 9, 6, 4, 3])
