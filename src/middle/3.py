"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

"""
解题思路：
使用两指针，一个字符哈希统计,一个实时的长度统计
左指针指向起始字符，右指针向右移动，移动时并统计字符出现次数，实时长度+1
当一个字符重复出现时，更新最长字符长度，并左指针向右移动一步，右指针到相同位置,实时长度置1
当左指针移动到最后是结束,判断实时长度是否大于最大长度

特殊情况：
空字符串：0
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left = 0
        right = 0
        statistic = {s[right]: 1}
        maxLength = 0
        currentLength = 1
        length = len(s)

        while left < length:
            right = right + 1
            if right >= length:
                left = left + 1
                right = left
                if currentLength > maxLength:
                    maxLength = currentLength
                currentLength = 1
                if left < length:
                    statistic = {s[right]: 1}
                else:
                    statistic = {}
                continue

            c = s[right]
            if c in statistic:
                tempLength = right - left
                if tempLength > maxLength:
                    maxLength = tempLength
                left = left + 1
                right = left
                if currentLength > maxLength:
                    maxLength = currentLength
                currentLength = 1
                if left < length:
                    statistic = {s[right]: 1}
                else:
                    statistic = {}
            else:
                statistic[s[right]] = 1
                currentLength = currentLength + 1
        if currentLength > maxLength:
            maxLength = currentLength
        print(maxLength)
        return maxLength


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("a") == 1
    assert s.lengthOfLongestSubstring("aa") == 1
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("au") == 2
