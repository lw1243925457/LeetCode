"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


解题思路：
pow(x,n)=pow(x,n/2) * pow(x,n/2)
当你为奇数时，最后再乘与一个n即可
边界条件没考虑好
缓存加二分，应该是logN的时间复杂度
"""
class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            if n < 0:
                return 1 / (self.myPow(x, (-n) // 2) * self.myPow(x, (-n) // 2))
            else:
                return self.myPow(x, n // 2) * self.myPow(x, n // 2)
        else:
            if n < 0:
                return 1 / (self.myPow(x, (-n) // 2) * self.myPow(x, (-n) // 2) * x)
            else:
                return self.myPow(x, n // 2) * self.myPow(x, n // 2) * x


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2.00000, 10))
    print(solution.myPow(2.00000, -2))
