"""
5452. 判断能否形成等差数列 显示英文描述
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个数字数组 arr 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。



示例 1：

输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
示例 2：

输入：arr = [1,2,4]
输出：false
解释：无法通过重新排序得到等差数列。


提示：

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return True
        arr = self.quick_sort(arr, 0, len(arr) - 1)
        dif = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != dif:
                return False
        return True

    def quick_sort(self, collection, low, high):
        # 快速排序
        if low >= high:
            return collection
        else:
            pivot = collection[low]  # 把第一个作为基准值
            left = low
            right = high
            while left < right:
                while left < right and collection[right] >= pivot:
                    right -= 1  # 右边的哨兵左移一个
                collection[left] = collection[right]
                while left < right and collection[left] <= pivot:
                    left += 1  # 左边的哨兵右移一个
                collection[right] = collection[left]
            collection[right] = pivot  # 两个哨兵相遇时则说明找到基准值的位置
            self.quick_sort(collection, low, left - 1)  # 递归左半部分
            self.quick_sort(collection, left + 1, high)  # 递归右半部分
            return collection


if __name__ == "__main__":
    s = Solution()
    assert s.canMakeArithmeticProgression([3, 5, 1])
    assert not s.canMakeArithmeticProgression([1, 2, 4])
