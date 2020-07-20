"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
from typing import List


class Solution:
    def __init__(self):
        self.digit2Char = {
            "1": [],
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.digitsConvert(digits, 0, "")

    def digitsConvert(self, digits, index, temp):
        if len(digits) - 1 == index:
            if digits[index] == '1':
                return [temp]
            l = []
            for c in self.digit2Char[digits[index]]:
                l.append(temp + c)
            return l

        if digits[index] == '1':
            return self.digitsConvert(digits, index+1, temp)
        res = []
        for c in self.digit2Char[digits[index]]:
            l = self.digitsConvert(digits, index+1, temp + c)
            for item in l:
                res.append(item)
        return res


if __name__ == "__main__":
    s = Solution()
    print(len(s.letterCombinations("23")), s.letterCombinations("23"))
    print(len(s.letterCombinations("234")), s.letterCombinations("234"))
    print(len(s.letterCombinations("231")), s.letterCombinations("231"))
    print(len(s.letterCombinations("123")), s.letterCombinations("123"))
