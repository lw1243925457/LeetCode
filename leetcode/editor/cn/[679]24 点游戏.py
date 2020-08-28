# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。 
# 
#  示例 1: 
# 
#  输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 1, 2]
# 输出: False
#  
# 
#  注意: 
# 
#  
#  除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。 
#  每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允
# 许的。 
#  你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。 
#  
#  Related Topics 深度优先搜索 
#  👍 161 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
from typing import List


class Solution:
    """解题思路：
    一、全排列枚举计算
    1.枚举所有数字的组合，4^4种
    2.组合之间两两进行计算,这里对(((a*b)*c)*d)和(a*b)*(c*d)分别进行了处理，他们好像是不包含的
    3.结果出现24则返回True，一直没有则false
    因为数字组合数固定，计算符组合也固定，则时间复杂度为常数O(1)

    注：添加了一个计算缓存，避免重复计算


    变形：
    1.如何获得所有可能的24的组合
    找出来还是容易的，但正确的输出有点麻烦。。。。。
    难道要数字加计算符全排列？
    """

    def __init__(self):
        self.results = []

    def judgePoint24(self, nums: List[int]) -> bool:
        arranges = []
        self._arrange(nums, arranges, [])
        for arrange in arranges:
            # if self._canGet24(arrange):
            #     return True
            # self._canGet24(arrange)
            expresions = []
            self._getAllexp(arrange, [str(arrange[0])], 1, expresions)
            print(expresions)
            for exp in expresions:
                print(exp, end= " ")
                print(eval(exp))
                if eval(exp) == 24:
                    print(exp)
        # print("等于24的组合如下：")
        # for result in self.results:
        #     print(result)
        return False

    def _getAllexp(self, arrange, path, index, expresions):
        if index >= 4:
            exp = path.copy()
            # expresions.append("".join(exp))
            expresions.append(exp)
            return
        for cal in ["+", "-", "*", "/"]:
            if (cal == "*" or cal == "/") and (arrange[index] == 0 or arrange[index-1] == 0):
                continue
            path.append(cal)
            path.append(str(arrange[index]))
            self._getAllexp(arrange, path, index+1, expresions)
            path.pop()
            path.pop()

    def _addBracket(self, expressions, index):
        eprB = []
        for i in range(0, )

    def _arrange(self, nums, arranges, path):
        """数字全排列"""
        if len(path) == 4:
            arranges.append(path.copy())
            return

        for i in range(0, len(nums)):
            path.append(nums[i])
            self._arrange(nums[:i] + nums[i+1:], arranges, path)
            path.pop()

    def _canGet24(self, arrange):
        """两两直接计算"""
        print("arrange:", arrange)
        for val1 in self._compute(arrange[0], arrange[1]):
            for val2 in self._compute(val1, arrange[2]):
                for val3 in self._compute(val2, arrange[3]):
                    if abs(val3-24.0) < 1e-5:
                        return True
        for val1 in self._compute(arrange[0], arrange[1]):
            for val2 in self._compute(arrange[2], arrange[3]):
                for val3 in self._compute(val1, val2):
                    if abs(val3-24.0) < 1e-5:
                        return True
        return False

    def _compute(self, lvals, rvals):
        """返回两数直接可能的计算结果"""
        res = [lvals + rvals, lvals - rvals, rvals + lvals, rvals - lvals]
        if lvals != 0 and rvals != 0:
            res += [lvals * rvals, rvals / lvals, lvals / rvals]
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # assert not solution.judgePoint24([1, 2, 1, 2])
    # assert not solution.judgePoint24([1, 5, 9, 1])
    # assert solution.judgePoint24([1, 8, 2, 5])
    # assert solution.judgePoint24([3, 9, 7, 7])
    # assert solution.judgePoint24([1, 9, 1, 2])
    # Solution().judgePoint24([1, 9, 1, 2])
    Solution().judgePoint24([3, 9, 7, 7])

