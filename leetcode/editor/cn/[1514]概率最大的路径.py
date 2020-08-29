# 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 
# 的一条无向边，且该边遍历成功的概率为 succProb[i] 。 
# 
#  指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。 
# 
#  如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, e
# nd = 2
# 输出：0.25000
# 解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, e
# nd = 2
# 输出：0.30000
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# 输出：0.00000
# 解释：节点 0 和 节点 2 之间不存在路径
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 10^4 
#  0 <= start, end < n 
#  start != end 
#  0 <= a, b < n 
#  a != b 
#  0 <= succProb.length == edges.length <= 2*10^4 
#  0 <= succProb[i] <= 1 
#  每两个节点之间最多有一条边 
#  
#  Related Topics 图 
#  👍 31 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque
from typing import List


class Solution:
    """
    解题思路：
    一、DFS暴力求解：遍历所有路径，输出最大概率
    注意点是双向边
    复杂度太高了没有过

    二、BFS暴力求解，因为边都是介于0和1之间，相乘的话会越来越小，则可以找到最短的几条路径，取最大值即可
    好像不行啊，加了权重就不能使用BFS了？
    """
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        nodes = defaultdict(list)
        for i in range(0, len(edges)):
            nodes[edges[i][0]].append([edges[i][1], succProb[i]])
            nodes[edges[i][1]].append([edges[i][0], succProb[i]])
        # ratios = [0]
        # self._dfs(nodes, start, end, [start], 1, ratios, n)
        # print(ratios)
        # return max(ratios)
        return self._bfs(nodes, start, end)

    def _dfs(self, nodes, start, end, visited, ratio, ratios, nodeAmount):
        if len(visited) == nodeAmount:
            return
        for item in nodes[start]:
            if item[0] == end:
                ratios.append(ratio * item[1])
            else:
                self._dfs(nodes, item[0], end, visited.copy() + [item[0]], ratio * item[1], ratios, nodeAmount)

    def _bfs(self, nodes, start, end):
        quque = deque([[start, 1]])
        visited = {start: 0}
        ratio = 0
        while len(quque) != 0:
            node = quque.popleft()
            for nextNode in nodes[node[0]]:
                nextRatio = nextNode[1] * node[1]
                if nextNode[0] == end:
                    ratio = max(ratio, nextRatio)
                elif nextRatio > ratio and (nextNode[0] not in visited or visited[nextNode[0]] < nextRatio):
                    visited[nextNode[0]] = nextRatio
                    quque.append([nextNode[0], nextRatio])
        return ratio


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end=2) == 0.250000
    assert Solution().maxProbability(5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4) == 0.2139
    # assert Solution().maxProbability(10, [[0,3],[1,7],[1,2],[0,9]], [0.31,0.9,0.86,0.36], 2, 3) == 0.2139
