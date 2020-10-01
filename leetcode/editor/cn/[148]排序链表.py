# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。 
# 
#  示例 1: 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2: 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5 
#  Related Topics 排序 链表 
#  👍 754 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    解题思路：
    一、快速排序：感觉是暗示了，栈应该不算空间
    """
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        self._quickSort(head, None)
        return head

    def _quickSort(self, head, tail):
        if head is tail:
            return head

        mid = self._partition(head, tail)
        showList(head, tail)

        print("start left:")
        self._quickSort(head, mid)
        print("start right:")
        self._quickSort(mid.next, tail)

    def _partition(self, head, tail):
        print("partition:")
        mid = head
        cur = head.next
        while cur and cur is not tail:
            if cur.val < mid.val:
                cur.next = head
                head = cur

        
# leetcode submit region end(Prohibit modification and deletion)


def showList(head, tail):
    p = head
    while p and p is not tail:
        print(p.val, end=" ")
        p = p.next
    print()


if __name__ == "__main__":
    head = ListNode(-1)
    head.next = ListNode(5)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)

    Solution().sortList(head)

    print("result:")
    showList(head, None)
