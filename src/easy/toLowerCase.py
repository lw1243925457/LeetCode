#!/usr/bin/env python
# @Time    : 2019/3/18 20:21
# @Author  : LiuWei
# @Site    : 
# @File    : toLowerCase.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 709. 转换成小写字母
"""
这题难道有什么特别的技巧，很难上80%
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ''
        ascii_A = ord('A')
        asscii_a = ord('a')
        for char in str:
            if char >= 'A' and char <= 'Z':
                result += chr(ord(char) + asscii_a - ascii_A)
            else:
                result += char
        # return str(string).lower()
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.toLowerCase("kjJjk"))