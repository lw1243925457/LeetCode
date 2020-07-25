"""
23. 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6


解题思路：
使用两个有序链表合并的思路，先两两合并，再两两合并合并后的链表,这个时间消耗在递归栈方面？
最优解是全部读取，然后使用排序，时间复杂度也就最优排序
"""
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        for item in lists:
            while item:
                l.append(item.val)
                item = item.next

        if len(l) == 0:
            return None
        l = sorted(l)
        p = ListNode(l[0])
        head = p
        for i in range(1, len(l)):
            p.next = ListNode(l[i])
            p = p.next
        return head

    # 使用两个有序链表合并的思路，先两两合并，再两两合并合并后的链表
    def s1(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        n = len(lists)
        nlists = []
        for i in range(0, n, 2):
            if i + 1 >= n:
                nlists.append(self.merge(lists[i], None))
            else:
                nlists.append(self.merge(lists[i], lists[i+1]))
        return self.mergeKLists(nlists)

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l = []
        while l1 is not None or l2 is not None:
            if l1 is None:
                l.append(l2.val)
                l2 = l2.next
            elif l2 is None:
                l.append(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                l.append(l1.val)
                l1 = l1.next
            else:
                l.append(l2.val)
                l2 = l2.next

        if len(l) == 0:
            return None
        p = ListNode(l[0])
        head = p
        for i in range(1, len(l)):
            p.next = ListNode(l[i])
            p = p.next
        return head


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    ans = s.mergeKLists([l1, l2, l3, l4])
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
