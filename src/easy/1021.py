#!/usr/bin/env python
# @Time    : 2019/6/17 6:51
# @Author  : LiuWei
# @Site    : 
# @File    : 1021.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
1021. Remove Outermost Parentheses
Easy

121

176

Favorite

Share
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.



Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string

需要去掉最外面的大括号,找到成对的大括号去掉
1.如果当前字符="(",计数器+1,begin为负数时,begin为当前序号
2.如果当前字符="(",计数器+1
3.如果当前字符=")",计数器-1,begin为0,end为当前序号,得到第一个去除大括号后的字符串:S[begin,end],begin置为-1
4.如果当前字符=")",计数器-1,begin不为0,继续遍历

Runtime: 44 ms, faster than 80.45% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 13.3 MB, less than 38.48% of Python3 online submissions for Remove Outermost Parentheses.
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        begin = -1
        count = 0

        for i in range(0, len(S)):
            char = S[i]
            if char == "(":
                count = count + 1
                if begin == -1:
                    begin = i
            elif char == ")":
                count = count - 1
                if count == 0:
                    result = result + S[begin + 1:i]
                    begin = -1
        print(result)
        return result


if __name__ == "__main__":
    solution = Solution()
    S = "(()())(())"
    assert solution.removeOuterParentheses(S) == "()()()"

    S = "(()())(())(()(()))"
    assert solution.removeOuterParentheses(S) == "()()()()(())"

    S = "()()"
    assert solution.removeOuterParentheses(S) == ""
