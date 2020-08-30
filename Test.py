from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4:
            return []

        nums = sorted(nums)
        ans = []

        for i in range(0, size - 3):
            if nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, size - 2):
                if nums[j] == nums[j - 1]:
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


if __name__ == "__main__":
    print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
    print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2, 3, 3, -3, 4], target=0))
