# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。 
# 
#  请注意，你可以假定字符串里不包括任何不可打印的字符。 
# 
#  示例: 
# 
#  输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
#  
#  Related Topics 字符串 
#  👍 56 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        isSpace = True
        for c in s:
            if c == " ":
                isSpace = True
            elif isSpace:
                ans += 1
                isSpace = False
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    assert solution.countSegments(" ") == 0
    assert solution.countSegments("") == 0
    assert solution.countSegments("Hello, my name is John") == 5
