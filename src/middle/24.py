"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
通过次数128,976提交次数194,796


解题思路：
首先建立一个初始节点，下一个节点指向列表的头节点
判断当前节点是否有下一个节点，没有就交互结束
有就交换，以0->1->2->3举例，当前是在1
0 -> 2
2 -> 1
1 -> 3
pre, cur, next, nnext 指针变量，初始NOne
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        root = ListNode(-1)
        root.next = head

        pre = root
        cur = head
        next = cur.next
        while cur is not None and next is not None:
            nnext = next.next
            pre.next = next
            next.next = cur
            cur.next = nnext

            pre = cur
            cur = nnext
            if cur is None:
                break
            next = cur.next

        return root.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ans = s.swapPairs(head)
    while ans:
        print(ans.val)
        ans = ans.next
