# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。 
# 
#  如果小镇的法官真的存在，那么： 
# 
#  
#  小镇的法官不相信任何人。 
#  每个人（除了小镇法官外）都信任小镇的法官。 
#  只有一个人同时满足属性 1 和属性 2 。 
#  
# 
#  给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。 
# 
#  如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 2, trust = [[1,2]]
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：N = 3, trust = [[1,3],[2,3]]
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入：N = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
#  
# 
#  示例 4： 
# 
#  输入：N = 3, trust = [[1,2],[2,3]]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 1000 
#  trust.length <= 10000 
#  trust[i] 是完全不同的 
#  trust[i][0] != trust[i][1] 
#  1 <= trust[i][0], trust[i][1] <= N 
#  
#  Related Topics 图 
#  👍 77 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、根据入度和出度来判断
    法官的入度为0，出度为n-1,则遍历统计每个人的出度和入度，最后判断是否有符合的人即可
    """

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1

        statistical = {}
        for i in range(0, len(trust)):
            if trust[i][0] not in statistical:
                statistical[trust[i][0]] = {"in": 0, "out": 1}
            else:
                statistical[trust[i][0]]["out"] = statistical[trust[i][0]]["out"] + 1
            if trust[i][1] not in statistical:
                statistical[trust[i][1]] = {"in": 1, "out": 0}
            else:
                statistical[trust[i][1]]["in"] = statistical[trust[i][1]]["in"] + 1
        for people in statistical.keys():
            if statistical[people]["out"] == 0 and statistical[people]["in"] == N-1:
                return people
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
