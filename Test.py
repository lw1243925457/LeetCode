from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4:
            return []

        nums = sorted(nums)
        ans = []

        for i in range(0, size - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, size - 2):
                if j != i+1 and nums[j] == nums[j - 1]:
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


import sys

import sys


def getResult(nums, ans, level):
    print(level, ans)
    if len(ans) > 9:
        return

    if level == 1:
        for num in nums:
            ans.append(num)
    if level == 2:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    ans.append(nums[i]*10+nums[j])
    getResult(nums, ans, level+1)

def isRepeat(nums):
    statistic = {}
    for num in nums:
        statistic[num] = statistic.get(num, 0) + 1
        if statistic[num] > 1:
            return False
    return True


if __name__ == "__main__":
    # 1,4,8 81
    nums = [8, 5, 9]
    maxnum = max(nums) - 1
    if 0 in nums or (2 in nums and 5 in nums) or (6 in nums and 9 in nums):
        print(-1)
    if 2 in nums:
        nums.append(5)
    elif 5 in nums:
        nums.append(2)
    if 6 in nums:
        nums.append(9)
    elif 9 in nums:
        nums.append(6)
    nums.sort()
    ans = []
    getResult(nums, ans, 1)
    print(ans[maxnum])

