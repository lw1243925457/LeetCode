"""
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
通过次数67,553提交次数132,241


解题思路：
记录n之前的指针pre，m之后的指针end
反转n到m之间的数据
pre指向m，n指向end
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        root = ListNode(0)
        root.next = head

        # 找到反转前n前一个位置
        pre = root
        for _ in range(1, m):
            pre = pre.next

        # 反转m到n之间，找到反转后n后一个位置
        start = pre.next
        end = start.next
        for _ in range(m, n):
            next = end.next
            end.next = start
            start = end
            end = next

        # pre指向n，m指向end
        pre.next.next = end
        pre.next = start
        return root.next


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    solution = Solution()
    solution.reverseBetween(l, 2, 4)
    while l:
        print(l.val, end=" ")
        l = l.next
