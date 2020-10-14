# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不
# 是 4 次，则需要在最终答案中包含该字符 3 次。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：["bella","label","roller"]
# 输出：["e","l","l"]
#  
# 
#  示例 2： 
# 
#  输入：["cool","lock","cook"]
# 输出：["c","o"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 100 
#  1 <= A[i].length <= 100 
#  A[i][j] 是小写字母 
#  
#  Related Topics 数组 哈希表 
#  👍 127 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        size = len(A)
        if size == 1:
            return list(A[0])

        hash = {}
        for c in A[0]:
            hash[c] = hash.get(c, 0) + 1

        for i in range(1, size):
            temp = {}
            for c in A[i]:
                temp[c] = temp.get(c, 0) + 1

            for key in hash:
                hash[key] = min(hash.get(key, 0), temp.get(key, 0))

        ans = []
        for key in hash:
            for i in range(0, hash.get(key, 0)):
                ans.append(key)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().commonChars(["cool"]) == ['c', 'o', 'o', 'l']
    assert Solution().commonChars(["cool", "lock", "cook"]) == ['c', 'o']
