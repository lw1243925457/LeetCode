"""
415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
通过次数44,773提交次数88,657


解题思路：
1刷
就用十进制加法模拟，从字符串尾部开始
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1

        ans = ""
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0:
            v1 = 0 if p1 < 0 else int(num1[p1])
            v2 = 0 if p2 < 0 else int(num2[p2])
            value = v1 + v2 + carry
            ans += str(value % 10)
            carry = value // 10
            p1 -= 1
            p2 -= 1
        if carry == 1:
            ans += str(carry)
        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings("", "1"))
    print(s.addStrings("23", ""))
    print(s.addStrings("134", "123"))
    print(s.addStrings("138", "123"))
    print(s.addStrings("1138", "123"))
    print(s.addStrings("1138", "19123"))
    print(s.addStrings("9", "1"))
