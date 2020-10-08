# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性： 
# 
#  
#  每行的元素从左到右升序排列。 
#  每列的元素从上到下升序排列。 
#  
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
#  Related Topics 二分查找 分治算法 
#  👍 444 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        height, width = len(matrix), len(matrix[0])
        index = 0
        while index < min(height, width):
            if matrix[index][index] == target or matrix[index][width-1] == target or matrix[height-1][index] == target:
                return True

            if matrix[index][index] < target < matrix[index][width-1]:
                left, right = index, width-1
                while left < right:
                    mid = (left + right) // 2
                    if matrix[index][mid] == target or matrix[index][left] == target or matrix[index][right] == target:
                        return True
                    elif matrix[index][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

            if matrix[index][index] < target < matrix[height-1][index]:
                left, right = index, height - 1
                while left < right:
                    mid = (left + right) // 2
                    if matrix[mid][index] == target or matrix[left][index] == target or matrix[right][index] == target:
                        return True
                    elif matrix[mid][index] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

            index += 1
        return False

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert not Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
    assert Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
    assert not Solution().searchMatrix([[1, 2]], 0)
    assert not Solution().searchMatrix([[1],[3],[5]], 2)