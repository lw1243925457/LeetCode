# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针 
#  👍 553 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4:
            return []

        nums = sorted(nums)
        ans = []

        for i in range(0, size - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, size - 2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, size - 1
                while left < right:
                    movel, mover = False, False
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        movel, mover = True, True
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        mover = True
                    else:
                        movel = True

                    # print(left, right, movel, mover)
                    if movel:
                        while left < right and nums[left] == nums[left + 1]:
                            left = left + 1
                        left = left + 1
                    if mover:
                        while left < right and nums[right] == nums[right - 1]:
                            right = right - 1
                        right = right - 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
    print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2, 3, 3, -3, 4], target=0))
    print(Solution().fourSum(nums=[0, 0, 0, 0], target=0))
