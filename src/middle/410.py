"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
通过次数153,248提交次数202,076


解题思路：
首先生成左括号，接下来面临两个选择，生成右括号或下一个左括号
使用递归解决
通过第一名的提交代码获取的技巧：通过一个全局变量去保存结果，感觉不错
"""
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.create('', n, n)
        return self.ans

    def create(self, content, left, right):
        # 结束条件，左括号用完，剩一个右括号
        if left == 0 and right == 1:
            self.ans.append(content + ")")

        # 生成左括号或右括号，但右括号生成的前提是前面有单的左括号
        if left > 0:
            self.create(content + "(", left - 1, right)
        if right > 0 and left < right:
            self.create(content + ")", left, right - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
