# 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。 
# 
#  第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。 
# 
#  返回一个表示节点 i 与其他所有节点距离之和的列表 ans。 
# 
#  示例 1: 
# 
#  
# 输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释: 
# 如下为给定的树的示意图：
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# 
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
#  
# 
#  说明: 1 <= N <= 10000 
#  Related Topics 树 深度优先搜索 
#  👍 114 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N < 2:
            return [0]

        graph = {}
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]

        ans = []
        for i in range(0, N):
            ans.append(self._pathCount(i, graph))
        return ans

    def _pathCount(self, node, graph):
        amount = 0
        distance = 1
        stack = [node]
        visited = set()
        visited.add(node)
        while stack:
            # print(stack, amount)
            size = len(stack)
            for i in range(0, size):
                children = graph[stack.pop(0)]
                for item in children:
                    if item not in visited:
                        amount += distance
                        visited.add(item)
                        stack.append(item)
            # print(stack, amount)
            distance += 1
        return amount


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == [8, 12, 6, 10, 10, 10]
