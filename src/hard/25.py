"""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
通过次数86,337提交次数138,984


解题思路：
大致思路和上一题两两反转一致，但反转操作发生变化,示例：
0 -> 1 -> 2 -> 3 -> 4, k=3
0 -> 3 -> 2 -> 1 -> 4
pre:0, cur:1, end:3, next:4

# 反转cur 到 end
cur - end : convert
    end.next = None
    cnext = cur.next
    temp = cnext
    cnext = cur
    cur = temp

# 反转后cur变到了end位置，重置pre和cur
pre -> cur
cur -> next
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head

        root = ListNode(-1)
        root.next = head

        pre = root
        cur = head
        while cur is not None:
            count = 1
            end = cur
            while end is not None and count < k:
                end = end.next
                count = count + 1

            if end is None:
                break

            print("Start convert:", pre.val, cur.val, end.val, k)
            next = end.next
            end.next = None
            tcur = cur
            cnext = cur.next
            while cnext is not None:
                temp = cnext.next
                cnext.next = tcur
                tcur = cnext
                cnext = temp

            pre.next = end
            cur.next = next

            pre = cur
            cur = next
            t = root
            while t:
                print(t.val, end=" ")
                t = t.next
            print("")

        return root.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    ans = s.reverseKGroup(head, 3)
    while ans:
        print(ans.val)
        ans = ans.next
