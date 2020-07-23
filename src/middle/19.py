"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

通过次数200,802提交次数514,335
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        empty = ListNode(0)
        empty.next = head

        right = empty
        for i in range(0, n+1):
            right = right.next

        left = empty
        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return empty.next


if __name__ == "__main__":
    s = Solution()

    root = ListNode(1)
    s.removeNthFromEnd(root, 1)
    while root is not None:
        print(root.val)
        root = root.next

    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    s.removeNthFromEnd(root, 2)
    while root is not None:
        print(root.val)
        root = root.next
