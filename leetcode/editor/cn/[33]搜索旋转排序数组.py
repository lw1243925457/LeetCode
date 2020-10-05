# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  你可以假设数组中不存在重复的元素。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  示例 1: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1 
#  Related Topics 数组 二分查找 
#  👍 989 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # print(left, right, mid, nums[left], nums[right], nums[mid])
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            if nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return -1

        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().search([5, 1, 2, 3, 4], 1) == 1
    assert Solution().search([4, 5, 6, 7, 8, 9, 1, 2, 3], 1) == 6
    assert Solution().search([1, 0], 1) == 0
    assert Solution().search([1], 1) == 0
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
