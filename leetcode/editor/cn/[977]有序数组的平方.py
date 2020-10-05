# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#  
# 
#  示例 2： 
# 
#  输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A 已按非递减顺序排序。 
#  
#  Related Topics 数组 双指针 
#  👍 125 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = -1
        while left + 1 < len(A):
            if A[left + 1] < 0:
                left += 1
            else:
                break

        right = left + 1
        ans = []
        while left > -1 or right < len(A):
            if left < 0:
                ans.append(A[right] ** 2)
                right += 1
                continue
            if not right < len(A):
                ans.append(A[left] ** 2)
                left -= 1
                continue
            if abs(A[left]) < abs(A[right]):
                ans.append(A[left] ** 2)
                left -= 1
            else:
                ans.append(A[right] ** 2)
                right += 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
