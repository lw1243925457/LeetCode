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
"""
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        result = self.convert(list(num), k, 0)
        print(''.join(result))
        return ''.join(result)

    def convert(self, num, k, current):
        # print("k:", k, "current:", current)
        if k < 1:
            return num
        if current >= len(num):
            return num

        minest = int(num[current])
        index = current
        length = len(num)
        if current + k + 1 < len(num):
            length = current + k + 1
        for i in range(current + 1, length):
            if minest > int(num[i]):
                index = i
                minest = int(num[i])
        if index == current:
            return self.convert(num, k, current + 1)

        minest = num[index]
        for i in range(index, current, -1):
            num[i] = num[i - 1]
        num[current] = minest
        # print(num, k, current, "index:", index, "minest:", minest, length)
        return self.convert(num, k - (index - current), current + 1)


if __name__ == "__main__":
    s = Solution()
    assert s.minInteger("4321", 4) == "1342"
    assert s.minInteger("100", 1) == "010"
    assert s.minInteger("36789", 1000) == "36789"
    assert s.minInteger("36789", 22) == "36789"
    assert s.minInteger("9438957234785635408", 23) == "0345989723478563548"
    assert s.minInteger("294984148179", 11) == "124498948179"
