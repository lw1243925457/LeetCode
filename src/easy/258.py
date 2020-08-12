"""
258. 各位相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？


解题思路：
递归：当为1返回；转字符串，相加
非递归可以使用n%10，再n=n//10,从个位数加
(num - 1) % 9 + 1,进阶解法很神，看不懂。。。。
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        s = str(num)
        amount = 0
        for c in s:
            amount += int(c)
        return self.addDigits(amount)