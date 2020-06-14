"""
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
"""

"""
将数字转换成字符串，使用左右指针，判断所指字符是否一直相等

边界考虑：
一位数，正数和负数的处理是否通用
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        length = len(num)
        begin = 0
        end = length - 1

        while begin < end:
            if num[begin] != num[end]:
                return False
            begin = begin + 1
            end = end - 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(1)
    assert not s.isPalindrome(-1)
    assert s.isPalindrome(121)
    assert s.isPalindrome(1221)
    assert not s.isPalindrome(123)
