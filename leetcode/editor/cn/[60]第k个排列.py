# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。 
# 
#  按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下： 
# 
#  
#  "123" 
#  "132" 
#  "213" 
#  "231" 
#  "312" 
#  "321" 
#  
# 
#  给定 n 和 k，返回第 k 个排列。 
# 
#  说明： 
# 
#  
#  给定 n 的范围是 [1, 9]。 
#  给定 k 的范围是[1, n!]。 
#  
# 
#  示例 1: 
# 
#  输入: n = 3, k = 3
# 输出: "213"
#  
# 
#  示例 2: 
# 
#  输入: n = 4, k = 9
# 输出: "2314"
#  
#  Related Topics 数学 回溯算法 
#  👍 321 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self._index = 0

    def getPermutation(self, n: int, k: int) -> str:
        if k == 0:
            return ""
        if n == 1:
            return "1"

        nums = []
        for i in range(1, n+1):
            nums.append(str(i))
        return self._recursive(nums, k, "")

    def _recursive(self, nums, k, path):
        # print(nums, k, self._index, path)
        if len(nums) == 0:
            self._index += 1
            if self._index == k:
                return path
            return None
        for i in range(0, len(nums)):
            res = self._recursive(nums[:i] + nums[i+1:], k, path+nums[i])
            if res:
                return res
        return None
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().getPermutation(3, 3))
