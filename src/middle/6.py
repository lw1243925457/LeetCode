"""
6. Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
通过次数138,770提交次数288,532


解题思路：
直观暴力解法：直接使用二维数组进行保存，然后读取返回
行数确定时，Z的高宽也确定，字符数也确定，为 row*3-2，
二维数组的高为行数，宽为：len（s) / (row / 2)
如果行数小于2，直接返回即可
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        array = []
        for i in range(0, numRows):
            array.append([])
            for j in range(0, len(s)):
                array[i].append(None)

        posx = 0
        posy = 0
        direction = 0
        for c in s:
            array[posx][posy] = c
            posx, posy, direction = self.adjustPos(posx, posy, direction, numRows)
            print(posx, posy, direction)

        result = ""
        for i in range(0, len(array)):
            for j in range(0, len(array[i])):
                if array[i][j] is not None:
                    result = result + array[i][j]

        # for a in array:
        #     print(a)
        print(result)
        return result

    def adjustPos(self, posx, posy, direction, numRows):
        # down
        if direction == 0:
            posx = posx + 1
            if posx >= numRows:
                posx = posx - 2
                posy = posy + 1
                if numRows > 2:
                    direction = 1
        # up
        else:
            posx = posx - 1
            if posx > 0:
                posy = posy + 1
            elif posx == 0:
                posy = posy + 1
                direction = 0
        return posx, posy, direction


if __name__ == "__main__":
    s = Solution()
    assert s.convert("LEETCODEISHIRING", 0) == "LEETCODEISHIRING"
    assert s.convert("LEETCODEISHIRING", 1) == "LEETCODEISHIRING"
    assert s.convert("LEETCODEISHIRING", 3) == "LCIRETOESIIGEDHN"
    assert s.convert("LEETCODEISHIRING", 4) == "LDREOEIIECIHNTSG"
    assert s.convert("ABCDE", 2) == "ACEBD"
    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 6) == "PAYPALISHIRING"
