"""
187. 重复的DNA序列
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。



示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]


解题思路：
1.从头开始遍历长度为10的子串，判断后面剩余的子串中是否包含10长度子串
一层遍历，一层查找，时间复杂度O(N^2)

2、从头遍历长度为10的子串，将其统计存入hash中，当统计值大于1时是重复子串，输出
一层遍历，一层遍历hash，两层同级，时间复杂度O(N)
"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        count = {}
        for i in range(0, len(s)-9):
            count[s[i:i+10]] = count.get(s[i:i+10], 0) + 1

        ans = []
        for key in count:
            if count[key] > 1:
                ans.append(key)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(solution.findRepeatedDnaSequences("AAAAAAAAAAA"))