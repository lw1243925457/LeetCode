# 爱丽丝有一手（hand）由整数数组给定的牌。 
# 
#  现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。 
# 
#  如果她可以完成分组就返回 true，否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
# 输出：true
# 解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。 
# 
#  示例 2： 
# 
#  输入：hand = [1,2,3,4,5], W = 4
# 输出：false
# 解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hand.length <= 10000 
#  0 <= hand[i] <= 10^9 
#  1 <= W <= hand.length 
#  
# 
#  
# 
#  注意：此题目与 1294 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-co
# nsecutive-numbers/ 
#  Related Topics Ordered Map 
#  👍 64 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、1.数组长度必须能整除分组数
        2.每组的起始牌为最小的牌，后面进行累计，如果没有，则不能构成要求
    """

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        size = len(hand) // W
        if W == 1:
            size = 1
        nums = {}
        for num in hand:
            nums[num] = nums.get(num, 0) + 1

        l = []
        for i in range(0, size):
            l = list(nums.keys())
            if len(l) == 0:
                return True
            minCard = min(l)
            # print(minCard, ",", end=" ")
            for j in range(0, W):
                # print(minCard + j, ":", nums.get(minCard + j, 0), end=" ")
                if nums.get(minCard + j, 0) < 1:
                    return False
                nums[minCard + j] = nums.get(minCard + j, 0) - 1
                if nums[minCard + j] < 1:
                    del nums[minCard + j]
            # print()
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNStraightHand(hand=[5, 1], W=1)
    assert not solution.isNStraightHand(hand=[5, 1], W=2)
    assert solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3)
    assert not solution.isNStraightHand(hand=[1, 2, 3, 4, 5], W=4)
    assert solution.isNStraightHand(hand=[1, 2, 3, 4, 5, 6], W=2)
