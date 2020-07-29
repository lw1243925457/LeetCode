"""
29. 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2



示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2


提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


解题思路：
看题意那就只能使用减法或加法了，而且不用四舍五入
减法：被除数循环减，记录次数，减不动了就返回次数
加法：除数循环加，记录次数，加后的树大于被除数就返回次数
负数先转正，返回的时候加上即可,考虑俩个都是负数的情况
记得判断是否溢出

前面的思路太慢了

正解应该是移位加夹逼。。。。。。
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isDividend = False
        if dividend < 0:
            isDividend = True
            dividend = -dividend

        isDivisor = False
        if divisor < 0:
            isDivisor = True
            divisor = -divisor

        # 符号相同就为正，符号不同就为负
        isNagetive = True
        if isDividend == isDivisor:
            isNagetive = False

        if dividend < divisor:
            return 0

        ans = 0
        if divisor == 1:
            ans = dividend
        else:
            while dividend >= divisor:
                count = 1
                temp = divisor
                while dividend >= (temp << 1):
                    temp = temp << 1
                    count = count << 1
                ans += count
                dividend -= temp

        if isNagetive:
            ans = -ans
        print(ans)
        MIN = -pow(2, 31)
        MAX = pow(2, 31) - 1
        if ans < MIN or ans > MAX:
            return MAX
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.divide(dividend=10, divisor=3) == 3
    assert s.divide(dividend=7, divisor=-3) == -2
    assert s.divide(dividend=-7, divisor=-3) == 2
    s.divide(dividend=2147483647, divisor=-2)
