"""
面试题 16.11. 跳水板
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：

0 < shorter <= longer
0 <= k <= 100000
通过次数8,210提交次数19,410


解题思路：
因为标记为简单，则直接使用递归暴力解......不行，这竟然是找规律的题，这突然体现数学思维的重要性了。。。。。。
"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k < 1:
            return []
        if shorter == longer:
            return [k*shorter]
        result = []
        for i in range(0, k+1):
            result.append(shorter * (k -i) + longer * i)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.divingBoard(1, 2, 3) == [3, 4, 5, 6]
