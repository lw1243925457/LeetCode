# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。 
# 
#  让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组： 
# 
#  
#  A.length >= 3 
#  在 0 < i < A.length - 1 条件下，存在 i 使得：
#  
#  A[0] < A[1] < ... A[i-1] < A[i] 
#  A[i] > A[i+1] > ... > A[A.length - 1] 
#  
#  
#  
# 
#  
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：[2,1]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：[3,5,5]
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：[0,3,2,1]
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  
# 
#  
# 
#  
#  Related Topics 数组 
#  👍 108 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        maxIndex = 0
        for i in range(0, len(A)):
            if A[i] > A[maxIndex]:
                maxIndex = i

        if maxIndex == 0 or maxIndex == (len(A) - 1):
            return False

        for i in range(0, maxIndex):
            if not A[i] < A[i + 1]:
                return False
        for i in range(maxIndex + 1, len(A)):
            if not A[i] < A[i - 1]:
                return False
        return True

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    assert not Solution().validMountainArray([2, 1])
    assert not Solution().validMountainArray([3, 5, 5])
    assert Solution().validMountainArray([0, 3, 2, 1])
    assert not Solution().validMountainArray([8, 7, 6])
    assert not Solution().validMountainArray([6, 7, 8])
