#!/usr/bin/env python
# @Time    : 2019/6/12 21:40
# @Author  : LiuWei
# @Site    : 
# @File    : 709.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
709. To Lower Case
Easy

274

949

Favorite

Share
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

Runtime: 28 ms, faster than 98.35% of Python3 online submissions for To Lower Case.
Memory Usage: 13.2 MB, less than 36.85% of Python3 online submissions for To Lower Case.

遍历字符串中的每个字符,如果字符在大写字母范围内,使用chr(ord(char) | 32)转换为小写字母

大写      十六进制         二进制            小写           十六进制        二进制
A          41                    0100 0001    a               61               0110 0001
B          42                    0100 0010    b               62               0110 0010
C          43                    0100 0011    c               63               0110 0011

对比发现，小写字符的ASCII的码值比大写字母大20H，同时大写字母二进制与小写字母二进制的区别在于第5为是0还是1（位数从0开始）。因此转换大小写思路有两种：
基于第一种比较的方式：首先判断是大写还是小写字母，然后加20H或者减20H
基于就修改二进制的方式：任何一个字母将第5位置1，则转成小写，置0则是大写。
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ''
        for char in str:
            if char >= 'A' and char <= 'Z':
                result += chr(ord(char) | 32)
            else:
                result += char
        return result


if __name__ == "__main__":
    solution = Solution()

    example = "Hello"
    assert "hello" == solution.toLowerCase(example)

    example = "hello"
    assert "hello" == solution.toLowerCase(example)

    example = "LOVELY"
    assert "lovely" == solution.toLowerCase(example)
