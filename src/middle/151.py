"""
151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。



示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


进阶：

请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。


解题思路：
1.手动实现split字符串，反转，重组

2.使用栈辅助实现
    1.遍历字符串，非空入栈
    2.遇到空字符，栈非空，栈中元素弹出（相当于子串逆序)
    3.如果最后栈非空，栈中元素弹出
每个元素平均访问两次，时间复杂度也就O(N)，但性能差距与调api差距比较大

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        使用栈辅助实现
        1.遍历字符串，非空入栈
        2.遇到空字符，栈非空，栈中元素弹出（相当于子串逆序)
        3.如果最后栈非空，栈中元素弹出
        :param s:
        :return:
        """
        ans = ""
        stack = []
        for c in s:
            if c != " ":
                stack.append(c)
            elif c == " " and len(stack) != 0:
                if ans != "":
                    ans += " "
                while len(stack) != 0:
                    ans += stack.pop()

        # 针对单个子串不需要加空格
        if len(stack) != 0 and ans != "":
            ans += " "
        while len(stack) != 0:
            ans += stack.pop()
        return ans[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
    print(solution.reverseWords("  hello world!  "))
    print(solution.reverseWords("a good   example"))
    print(solution.reverseWords("a"))
