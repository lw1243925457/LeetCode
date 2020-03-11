"""
1013. 将数组分成和相等的三个部分
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。



示例 1：

输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


提示：

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
通过次数8,967提交次数18,308
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        amount = sum(A)
        if amount % 3 != 0:
            return False
        average = int(amount / 3)
        print(average)

        indexi = -1
        amount = 0
        for i in range(0, len(A)):
            num = A[i]
            amount = amount + num
            if amount == average:
                indexi = i
                break
        print(indexi)
        if indexi < 0:
            return False

        indexj = indexi + 1
        while indexj < len(A) - 1:
            amount = amount + A[indexj]
            if amount == average * 2:
                print(indexj)
                return True
            else:
                indexj = indexj + 1
        print(indexj)

        print(average, indexi, indexj)
        return False


if __name__ == "__main__":
    s = Solution()

    data = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    assert s.canThreePartsEqualSum(data)

    data = [1, -1, 1, -1]
    assert not s.canThreePartsEqualSum(data)

    data = [12, -4, 16, -5, 9, -3, 3, 8, 0]
    assert s.canThreePartsEqualSum(data)
