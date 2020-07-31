"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
通过次数90,165提交次数270,569


解题思路：
还是看了题解。。。。。。。
还是用栈来解题，基本使用有效括号的判断
栈底元素始终为：最后一个没有匹配的的右括号下标，特殊情况前面全是有效，则开始在栈底放入-1,则可以正确计算有效程度
1.（坐标放入
2.）弹出栈定匹配
    栈为空，坐标放入
    栈不为空，栈顶弹出，）下标-栈顶下标表示此右括号最大有效长度，更新最大长度

题解的方法三的左右指定，前后两次遍历的思路也很厉害
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        stack = [-1]
        ans = 0
        for i in range(0, n):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses(")()())"))
