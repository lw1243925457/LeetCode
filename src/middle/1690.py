"""
面试题 17.13. 恢复空格
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数



示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。
通过次数2,790提交次数5,007


这种题目对应现在的我来说有点难，动态规划我还是没完全掌握，这题的反着匹配思维很妙
"""
from typing import List


class TrieTree:
    def __init__(self):
        self.array = [None] * 26
        self.isEnd = False

    def insert(self, string: str):
        root = self
        for i in range(len(string) - 1, -1, -1):
            charPos = ord(string[i]) - ord('a')
            if root.array[charPos] is None:
                root.array[charPos] = TrieTree()
            root = root.array[charPos]
        root.isEnd = True


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie = TrieTree()
        for string in dictionary:
            trie.insert(string)

        dp = [0] * (len(sentence) + 1)
        for i in range(1, len(sentence) + 1):
            dp[i] = dp[i - 1] + 1

            current = trie
            for j in range(i, 0, -1):
                pos = ord(sentence[j - 1]) - ord('a')
                if current.array[pos] is None:
                    break
                elif current.array[pos].isEnd:
                    dp[i] = min(dp[i], dp[j - 1])
                if dp[i] == 0:
                    break
                current = current.array[pos]
        print(dp[len(sentence)])
        return dp[len(sentence)]


if __name__ == "__main__":
    # trie = TrieTree()
    # trie.insert("aa")
    # trie.insert("bb")
    # print(trie.array)
    # print(trie.array[0].array)
    # print(trie.array[1].array)

    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"
    s = Solution()
    assert s.respace(dictionary, sentence) == 7
