# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 
# JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。 
# 
#  说明: 
# 
#  
#  如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排
# 序更靠前 
#  所有的机场都用三个大写字母表示（机场代码）。 
#  假定所有机票至少存在一种合理的行程。 
#  
# 
#  示例 1: 
# 
#  输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#  
# 
#  示例 2: 
# 
#  输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。 
#  Related Topics 深度优先搜索 图 
#  👍 167 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、从起始点出发，下一个点为自然排序最小的字母
        题目的隐藏条件还有所有的机场必须到包含在行程内，这个不通过用例，难看出来啊。。。。。。
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        size = len(tickets)
        if size < 2:
            return tickets[0]

        ticketsMap = {}
        airports = set()
        for ticket in tickets:
            ticketsMap[ticket[0]] = ticketsMap.get(ticket[0], []) + [ticket[1]]
            airports.add(ticket[0])
            airports.add(ticket[1])
        print(ticketsMap, airports)

        path = ["JFK"]
        visited = set()
        visited.add("JFK")
        return self.dfs(path, ticketsMap, size, visited, len(airports))

    def dfs(self, path, ticketsMap, size, visited, airportsAmounts):
        print("path:", path, size)
        if len(path) == (size + 1):
            print(len(visited), airportsAmounts, visited)
            if len(visited) == airportsAmounts:
                print(path)
                return path
            return None
        if len(ticketsMap.get(path[-1], [])) == 0:
            return None
        if len(path) > (size + 1):
            return None

        for ticket in sorted(ticketsMap[path[-1]]):
            path.append(ticket)
            visited.add(ticket)
            result = self.dfs(path, ticketsMap, size, visited, airportsAmounts)
            if result is not None:
                return result
            path.pop()
            if ticket in visited:
                visited.remove(ticket)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    assert solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"]
