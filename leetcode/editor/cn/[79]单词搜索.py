# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 562 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self._find(board, i, j, 0, word):
                    return True
        return False

    def _find(self, board, row, col, index, word):
        if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        temp = board[row][col]
        board[row][col] = "$"
        if self._find(board, row - 1, col, index + 1, word):
            board[row][col] = temp
            return True
        if self._find(board, row + 1, col, index + 1, word):
            board[row][col] = temp
            return True
        if self._find(board, row, col - 1, index + 1, word):
            board[row][col] = temp
            return True
        if self._find(board, row, col + 1, index + 1, word):
            board[row][col] = temp
            return True
        board[row][col] = temp
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist(board, "ABCCED")
    assert Solution().exist(board, "SEE")
    assert not Solution().exist(board, "ABCB")
    assert Solution().exist(board, "")
    assert Solution().exist(board, "A")
    print(board)
