"""
5508. 数的平方等于两数乘积的方法数 显示英文描述
通过的用户数445
尝试过的用户数781
用户总通过次数445
用户总提交次数1253
题目难度Medium
给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：

类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length
类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length


示例 1：

输入：nums1 = [7,4], nums2 = [5,2,8,9]
输出：1
解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)
示例 2：

输入：nums1 = [1,1], nums2 = [1,1,1]
输出：9
解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1
类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[j] * nums2[k]
类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]
示例 3：

输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7]
输出：2
解释：有两个符合题目要求的三元组
类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]
示例 4：

输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
输出：0
解释：不存在符合题目要求的三元组


提示：

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5
"""
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1, d2 = {}, {}
        for i in range(0, len((nums1))):
            d1[nums1[i]] = d1.get(nums1[i], []) + [i]
        for i in range(0, len((nums2))):
            d2[nums2[i]] = d2.get(nums2[i], []) + [i]
        # print(d1, d2)
        ans = 0
        ans += self._f(nums1, nums2, d2)
        ans += self._f(nums2, nums1, d1)
        # print(ans)
        return ans

    def _f(self, nums1, nums2, d):
        count = 0
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                p = nums1[i]**2
                if p < nums2[j] or p % nums2[j] != 0:
                    continue
                other = p // nums2[j]
                if other in d:
                    for index in d[other]:
                        if index > j:
                            count += 1
        return count


if __name__ == "__main__":
    assert Solution().numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]) == 1
    assert Solution().numTriplets(nums1 = [1,1], nums2 = [1,1,1]) == 9
    assert Solution().numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7]) == 2
    assert Solution().numTriplets(nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]) == 0
    assert Solution().numTriplets(nums1 = [3, 1, 2, 2], nums2 = [1, 3, 4, 4]) == 4
