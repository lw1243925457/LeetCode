"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。


提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
通过次数134,831提交次数294,511


思路及其不严谨啊，兄弟，太菜了。。。。。。
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        result = nums[0] + nums[1] + nums[2]
        if result == target:
            return result

        n = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                print(nums[i], nums[left], nums[right], tmp)
                if tmp == target:
                    return tmp
                if abs(tmp - target) < abs(result - target):
                    result = tmp
                if tmp > target:
                    rightt = right - 1
                    while rightt > left and nums[rightt] == nums[right]:
                        rightt = rightt - 1
                    right = rightt
                else:
                    leftt = left + 1
                    while leftt < right and nums[leftt] == nums[left]:
                        leftt = leftt + 1
                    left = leftt
        print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
    # assert s.threeSumClosest([-3, -2, -5, 3, -4], -1) ==
    assert s.threeSumClosest([0,2,1,-3], 1) == 0
    # assert s.threeSumClosest([1,2,4,8,16,32,64,128], 82)
    assert s.threeSumClosest([-1,0,1,1,55], 3) == 2
