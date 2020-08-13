"""
520. 检测大写字母
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。


解题思路：
如果首字母大写，则全大写或者剩余全小写
如果首字母小写，则全部小写
也就是首字母后都是全大写或小写就行

边界条件的考虑不周全。。。导致出了很多错
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n < 2:
            return True
        if 'A' <= word[1] <= 'Z' and 'a' <= word[0] <= 'z':
            return False

        l, r = 'a', 'z'
        if 'a' <= word[1] <= 'z':
            l, r = 'A', 'Z'

        for i in range(2, n):
            if l <= word[i] <= r:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.detectCapitalUse("ggg"))
    print(solution.detectCapitalUse("mL"))
    print(solution.detectCapitalUse("G"))
