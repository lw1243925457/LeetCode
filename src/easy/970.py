"""
970. 强整数
给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。



示例 1：

输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释：
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
示例 2：

输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]


提示：

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6


解题思路：
也就求x^i + y^j <= bound, i,j = 0,1,....

第一名的答案没太看懂。。。。。
class Solution:
    def powerfulIntegers(self,x, y, bound) :
        max_i=pow(bound,1/x)
        max_j=pow(bound,1/y)
        n =[]
        if x ==1:
            for j in range(0,int(max_j+3)):
                m =1+y**j
                if m<=bound:
                    n.append(m)
        else:
            for i in range(0,int(max_i+3)):
                for j in range(0,int(max_i+3)):
                    m =x**i+y**j
                    if m<=bound:
                        n.append(m)
        return set(n)
"""
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        # 2**18 > bound
        for i in range(0, 20):
            for j in range(0, 20):
                v = x ** i + y ** j
                if v <= bound:
                    ans.add(v)
        return list(ans)


if __name__ == "__main__":
    solution = Solution()
    print(solution.powerfulIntegers(x = 2, y = 3, bound = 10))
