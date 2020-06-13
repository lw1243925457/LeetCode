"""
7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

通过次数374,637提交次数1,092,871
"""

"""
正常解法：
数字转字符串，前后两个指针，指针所指相互交换，当两指针相遇时结束或者开始指针位置大于结束指针（既开始序号需要小于结束序号）

边界既特殊情况考虑：
负数：保留符号，对后面的数字进行反转
反转后前面为0：去掉前面的0
整数溢出：当溢出时返回0，pow(2, 31) - 1 = 2147483647
"""
class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if x < 0:
            num = str(-x)

        length = len(num)
        begin = 0
        end = length - 1

        convert = list(num)
        while begin < end:
            a = int(convert[begin])
            b = int(convert[end])
            a = a + b
            b = a - b
            a = a -b
            convert[begin] = str(a)
            convert[end] = str(b)

            begin = begin + 1
            end = end - 1

        num = int(''.join(convert))
        if num > pow(2, 31) - 1:
            return 0
        if x < 0:
            return -int(num)
        return int(num)


if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(320) == 23
    assert s.reverse(-320) == -23
    assert s.reverse(-10) == -1
    assert s.reverse(1534236469) == 0
