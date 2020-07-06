"""
5455. 最多 K 次交换相邻数位后得到的最小整数 显示英文描述
通过的用户数5
尝试过的用户数13
用户总通过次数5
用户总提交次数15
题目难度Hard
给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。

你可以交换这个整数相邻数位的数字 最多 k 次。

请你返回你能得到的最小整数，并以字符串形式返回。



示例 1：



输入：num = "4321", k = 4
输出："1342"
解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。
示例 2：

输入：num = "100", k = 1
输出："010"
解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。
示例 3：

输入：num = "36789", k = 1000
输出："36789"
解释：不需要做任何交换。
示例 4：

输入：num = "22", k = 22
输出："22"
示例 5：

输入：num = "9438957234785635408", k = 23
输出："0345989723478563548"


提示：

1 <= num.length <= 30000
num 只包含 数字 且不含有 前导 0 。
1 <= k <= 10^9


超出时间限制
暴力解不行，不规范，过会研究下正确的
"""
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k <= 0 or not num: return num

        # 这个是tricky的代码...不加会超时
        if len(num) ** 2 < k: return ''.join(sorted(list(num)))

        # 每次寻找前`k+1`个数字中的最小数字的最小下标，复杂度O(n^2)。。。
        index = num.index(min(num[:k + 1]))
        res = num[index] + self.minInteger(num[:index] + num[index + 1:], k - index)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.minInteger("4321", 4) == "1342"
    assert s.minInteger("100", 1) == "010"
    assert s.minInteger("36789", 1000) == "36789"
    assert s.minInteger("36789", 22) == "36789"
    assert s.minInteger("9438957234785635408", 23) == "0345989723478563548"
    assert s.minInteger("294984148179", 11) == "124498948179"
