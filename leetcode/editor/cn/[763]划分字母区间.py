# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心算法 双指针 
#  👍 260 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    还是没太看的懂，先copy
    """
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for i, c in enumerate(S):
            last[c] = i

        partition = []
        start, end = 0, 0
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition


# leetcode submit region end(Prohibit modification and deletion)
