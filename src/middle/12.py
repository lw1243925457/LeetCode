"""
12. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.


解题思路：
从左到右进行转换，遇到4,9进行特殊处理
官方的解答还是简洁明了啊
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        num2Roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        roman = ""

        s = str(num)
        if len(s) != 4:
            while (len(s) < 4):
                s = "0" + s
        one = int(s[3])
        ten = int(s[2])
        hundred = int(s[1])
        thousand = int(s[0])

        if thousand != 0:
            for i in range(0, thousand):
                roman = roman + "M"

        if hundred != 0:
            if hundred < 4:
                for i in range(0, hundred):
                    roman = roman + "C"
            elif hundred == 4:
                roman = roman + "CD"
            elif hundred < 9:
                roman = roman + "D"
                for i in range(0, hundred - 5):
                    roman = roman + "C"
            elif hundred == 9:
                roman = roman + "CM"

        if ten != 0:
            if ten < 4:
                for i in range(0, ten):
                    roman = roman + "X"
            elif ten == 4:
                roman = roman + "XL"
            elif ten < 9:
                roman = roman + "L"
                for i in range(0, ten - 5):
                    roman = roman + "X"
            elif ten == 9:
                roman = roman + "XC"

        if one != 0:
            if one < 4:
                for i in range(0, one):
                    roman = roman + "I"
            elif one == 4:
                roman = roman + "IV"
            elif one < 9:
                roman = roman + "V"
                for i in range(0, one - 5):
                    roman = roman + "I"
            elif one == 9:
                roman = roman + "IX"

        print(roman)
        return roman


if __name__ == "__main__":
    s = Solution()
    assert s.intToRoman(3) == "III"
    assert s.intToRoman(4) == "IV"
    assert s.intToRoman(9) == "IX"
    assert s.intToRoman(58) == "LVIII"
    assert s.intToRoman(1994) == "MCMXCIV"
