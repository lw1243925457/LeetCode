# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表 
#  👍 568 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    1.暴力法：逐个遍历元素，因为有负数，所有一直累加完所有元素，等于时累加结果
    两层遍历，时间复杂度为O(N^2),超时了。。。。。

    2.sum[i:j] = sum[0:j] - sum[0:i]，不妨将sum[i:j]设为k，于是可以转化为sum[0:j] - k = sum[0:i]
    就遍历了一次，时间复杂度O(N)
    这种思路是真的巧妙，我是没想到的
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, amount, size = 0, 0, len(nums)
        amountMap = {0: 1}
        for i in range(0, size):
            amount += nums[i]
            ans += amountMap.get(amount - k, 0)
            amountMap[amount] = amountMap.get(amount, 0) + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 1, 1], 4) == 0
    assert solution.subarraySum([4, 4, 4], 3) == 0
    assert solution.subarraySum([28, 54, 7, -70, 22, 65, -6], 100) == 1
