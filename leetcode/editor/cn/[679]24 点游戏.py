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
from typing import List


class Solution:
    """解题思路：
    一、全排列枚举计算
    1.枚举所有数字的组合，4^4种
    2.组合之间两两进行计算,这里对(((a*b)*c)*d)和(a*b)*(c*d)分别进行了处理，他们好像是不包含的
    3.结果出现24则返回True，一直没有则false
    因为数字组合数固定，计算符组合也固定，则时间复杂度为常数O(1)

    注：添加了一个计算缓存，避免重复计算

    二、两两计算：是我之前没能领略其正真含义，这个才是最佳的解法，计算后的结果也加入两两随机计算中，得到最后一个结果


    变形：
    1.如何获得所有可能的24的组合
    方法2改写下就行了，感觉差不多可以了，nice
    """

    def judgePoint24(self, nums: List[int]) -> bool:
        """
        # 输出24的计算表达式
        expressions = []
        for i in range(0, len(nums)):
            nums[i] = str(nums[i])
        self._getAllExpressions(nums, expressions)
        print(expressions)
        for expression in expressions:
            try:
                if eval(expression) == 24:
                    print(expression)
            except:
                continue
        return True
        """

        if len(nums) == 1:
            if abs(nums[0] - 24) < 1e-5:
                return True
            return False

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                for val in self._compute(nums[i], nums[j]):
                    temp = nums.copy()
                    temp.remove(nums[i])
                    temp.remove(nums[j])
                    temp.append(val)
                    if self.judgePoint24(temp):
                        return True
        return False

    def _compute(self, lvals, rvals):
        """返回两数直接可能的计算结果"""
        res = [lvals + rvals, lvals - rvals, rvals + lvals, rvals - lvals, lvals * rvals]
        if lvals != 0:
            res.append(rvals / lvals)
        if rvals != 0:
            res.append(lvals / rvals)
        return res

    def _getAllExpressions(self, nums, expressions):
        if len(nums) == 1:
            expressions.append(nums[0])
            return

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                for operation in ["+", "-", "*", "/"]:
                    temp = nums.copy()
                    temp.remove(nums[i])
                    temp.remove(nums[j])
                    for expression in self._getExpression(operation, nums[i], nums[j]):
                        self._getAllExpressions(temp + [expression], expressions)

    def _getExpression(self, operation, param1, param2):
        if operation == "+":
            return ["(%s+%s)" % (param1, param2)]
        if operation == "-":
            return ["(%s-%s)" % (param1, param2), "(%s-%s)" % (param2, param1)]
        if operation == "*":
            return ["(%s*%s)" % (param1, param2)]
        if operation == "/":
            res = []
            if param2 != 0:
                res.append("(%s/%s)" % (param1, param2))
            if param1 != 0:
                res.append("(%s/%s)" % (param2, param1))
            return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # assert not solution.judgePoint24([1, 2, 1, 2])
    # assert not solution.judgePoint24([1, 5, 9, 1])
    # assert solution.judgePoint24([1, 8, 2, 5])
    # assert solution.judgePoint24([3, 9, 7, 7])
    # assert solution.judgePoint24([1, 9, 1, 2])
    # assert solution.judgePoint24([3, 3, 8, 8])
    Solution().judgePoint24([1, 9, 1, 2])
    # Solution().judgePoint24([3, 9, 7, 7])
