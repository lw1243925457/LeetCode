"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


解题思路：
模拟手算乘法即可，关键点是进位
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "1" or num2 == "1":
            return num1
        if num1 == "0" or num2 == "0":
            return "0"

        def multi(num: int, mcarry: int) -> str:
            if num == 0: return "0"

            res = ""
            carry = 0
            for i in range(m - 1, -1, -1):
                amount = int(num2[i]) * num + carry
                res += str(amount % 10)
                carry = amount // 10

            if carry != 0:
                res += str(carry)
            res = res[::-1]

            for i in range(0, mcarry):
                res += "0"
            print("multi:", num, num2, mcarry, res)
            return res

        def addNums(add1: str, add2: str) -> str:
            l1, l2 = len(add1), len(add2)
            p1, p2 = l1-1, l2-1
            addCarry = 0
            res = ""

            while p1 > -1 or p2 > -1:
                value1, value2 = 0, 0
                if p1 > -1:
                    value1 = int(add1[p1])
                    p1 -= 1
                if p2 > -1:
                    value2 = int(add2[p2])
                    p2 -= 1
                amount = value1 + value2 + addCarry
                res += str(amount % 10)
                addCarry = amount // 10
            if addCarry != 0:
                res += str(addCarry)
            print("add:", add1, add2, res[::-1])
            return res[::-1]

        n, m = len(num1), len(num2)
        mcarry = 0
        last = "0"
        ans = ""

        for i in range(n-1, -1, -1):
            value = multi(int(num1[i]), mcarry)
            ans = addNums(value, last)
            last = ans
            mcarry += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.multiply("1", "23") == "23"
    assert s.multiply("13", "1") == "13"
    assert s.multiply("13", "") == "13"
    assert s.multiply("13", "0") == "0"
    assert s.multiply("123", "456") == "56088"
