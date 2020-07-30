"""
31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

通过次数77,336提交次数225,772


解题思路：
题目描述的有点让人迷糊，可能是自己的语文理解还是差了点。下面这位大兄弟的：我们可以将该问题形式化地描述为：给定若干个数字，将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数，很强，下面是思路：

```
如何得到这样的排列顺序？这是本文的重点。我们可以这样来分析：

我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
在尽可能靠右的低位进行交换，需要从后向前查找
将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列

作者：imageslr
链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return None

        l, r = n - 2, n - 1
        while l >= 0:
            if nums[l] < nums[r]:
                break
            l = l - 1
            r = r - 1

        if l < 0:
            nums.reverse()
            return None

        k = n - 1
        while 1:
            if nums[l] < nums[k]:
                break
            k = k - 1
        nums[l], nums[k] = nums[k], nums[l]

        start = r
        end = n - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end - 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 8, 5, 7, 6, 4]
    s.nextPermutation(nums)
    print(nums)

    nums = [5, 4, 3, 2, 1]
    s.nextPermutation(nums)
    print(nums)
