"""
309. 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
通过次数31,441提交次数57,738


参考官方题解：啥时候靠自己就能做出这样的题啊。。。。。。
一共有三种状态：
1.持有股票
2.没有股票，没有处于冻结
3.没有股票，处于冻结

状态转移：
1.持有股票：要么是当天买的（那前一天就处于状态2）；要么是以前买的（前一天处于状态1）
2.没有股票，不冻结：前一天没有卖买，处于状态2或者3
3.没有股票，处于冻结：前一天卖了，前一天处于状态1

最后一天持有股票，要么卖要么不卖
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        f1 = -prices[0]
        f2 = 0
        f3 = 0
        for i in range(1, len(prices)):
            f1 = max(f2 - prices[i], f1)
            f2 = max(f2, f3)
            f3 = f1 + prices[i]
        return max(f1, f2, f3)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
