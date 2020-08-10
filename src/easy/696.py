"""
696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。


解题思路：
子串数量必为偶数，总串规律如下
01--0011-000111==1,2,3
10-1100-111000
使用双指针，分别记录遍历0和1的数量
新一轮计数前，累加结果
每个数据最多访问一遍，时间复杂度N
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        ans = 0
        current, last = 1, 0
        find = False
        for i in range(1, n):
            if s[i] == s[i - 1]:
                current += 1
            else:
                if not find:
                    last = current
                    current = 1
                    find = True
                else:
                    ans += min(last, current)
                    last = current
                    current = 1

        if find:
            ans += min(last, current)

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBinarySubstrings("1"))
    print(solution.countBinarySubstrings("11"))
    print(solution.countBinarySubstrings("1100"))
    print(solution.countBinarySubstrings("1000"))
    print(solution.countBinarySubstrings("1000111"))
