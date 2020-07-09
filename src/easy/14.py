"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

通过次数305,640提交次数796,065

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


解题思路：
为所有的字符串构建trie树
选择启动一个长度最短在trie树中进行匹配即可（逐一从头匹配）
"""
from typing import List


class TrieTree:
    def __init__(self):
        self.array = [None] * 26

    def insert(self, s: str):
        current = self
        for c in s:
            pos = ord(c) - ord('a')
            if current.array[pos] is None:
                current.array[pos] = TrieTree()
            current = current.array[pos]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        trie = TrieTree()
        minStr = strs[0]
        for str in strs:
            trie.insert(str)
            if len(str) < len(minStr):
                minStr = str

        result = ""
        for i in range(0, len(minStr)):
            temp = ""
            current = trie
            j = i
            pos = ord(minStr[j]) - ord('a')
            # print(i, j, pos, current.array)
            while current.array[pos] is not None and self.otherIsNone(current.array, pos):
                temp += minStr[j]
                current = current.array[pos]
                j = j + 1
                if j >= len(minStr):
                    break
                pos = ord(minStr[j]) - ord('a')
                # print(i, j, pos, current.array)
            if len(temp) > len(result):
                result = temp
        # print(result)
        return result

    def otherIsNone(self, array, pos):
        for i in range(0, len(array)):
            if i != pos and array[i] is not None:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    assert s.longestCommonPrefix(strs) == "fl"
    strs = ["dog","racecar","car"]
    assert s.longestCommonPrefix(strs) == ""
