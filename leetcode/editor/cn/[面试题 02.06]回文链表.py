# 编写一个函数，检查输入的链表是否是回文的。 
# 
#  
# 
#  示例 1： 
# 
#  输入： 1->2
# 输出： false 
#  
# 
#  示例 2： 
# 
#  输入： 1->2->2->1
# 输出： true 
#  
# 
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 
#  👍 34 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    解题思路：
    一、快慢双指针：快指针一次走两步，慢指针一次走一步，慢指针边走边反转链表
    快这种走到头了，慢指针就是中间位置
    如果快指针最后走两步到终点，则链表为奇数，慢真正刚好为中心；反之，偶数，慢指针和其next为中心
    """
    def isPalindrome(self, head: ListNode) -> bool:
        low, fast = head, head
        left, right = head, head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                low = low.next
            elif fast.next and not fast.next.next:
                fast = fast.next.next
                left, right = low, low.next
            elif not fast.next:
                fast = fast.next
                left, right = low, low

        low = head
        self._convert(head, left)
        head.next = None

        while left and right:
            if not left.val == right.val:
                return False
        return True

    def _convert(self, node, left):
        if node is left:
            return left
        next = self._convert(node.next, left)
        next.next = node
        return node


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().isPalindrome()
