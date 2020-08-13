"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。



示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2


提示：你可以假定该字符串只包含小写字母。


解题思路：
遍历hash统计字符出现次数
遍历一次，判断当前字符出现次数，为1时返回，没有为1的最后返回-1
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i in range(0, len(s)):
            if count[s[i]] == 1:
                return i
        return -1