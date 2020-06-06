"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
通过次数438,421提交次数1,169,498
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p1 = l1
        p2 = l2
        p3 = []
        fore = 0
        while p1 is not None or p2 is not None:
            value1 = 0
            value2 = 0
            if p1 is not None:
                value1 = p1.val
                p1 = p1.next
            if p2 is not None:
                value2 = p2.val
                p2 = p2.next

            value = (value1 + value2 + fore) % 10
            fore = int((value1 + value2 + fore) / 10)
            p3.append(value)
            print((value2, value2, value, fore))

        if fore != 0:
            p3.append(fore)

        root = ListNode(p3[0])
        current = root
        for i in range(1, len(p3)):
            node = ListNode(p3[i])
            current.next = node
            current = current.next

        return root


def createListNode(array) -> ListNode:
    root = ListNode(array[0])
    current = root
    for i in range(1, len(array)):
        node = ListNode(array[i])
        current.next = node
        current = current.next
    return root


def showListNode(listNode: ListNode):
    res = []
    c = listNode
    while c is not None:
        res.append(c.val)
        c = c.next
    print(res)


if __name__ == "__main__":
    s = Solution()
    res = s.addTwoNumbers(createListNode([0, 8, 6, 5, 6, 8, 3, 5, 7]), createListNode([6, 7, 8, 0, 8, 5, 8, 9, 7]))
    showListNode(res)
