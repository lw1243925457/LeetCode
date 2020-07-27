"""
641. 设计循环双端队列
设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。
示例：

MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4



提示：

所有值的范围为 [1, 1000]
操作次数的范围为 [1, 1000]
请不要使用内置的双端队列库。
通过次数9,707提交次数18,427


解题思路：
1 刷

1.使用数组实现，但插入操作麻烦
2.使用链表实现，因为没有查询的操作，则使用链表实现了
"""


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.used = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.used = self.used + 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.used = self.used + 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.head is None:
            return False
        if self.used == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.used = self.used - 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        print("delete before:", self.tail.val, self.used)
        if self.tail is None:
            return False
        if self.used == 1:
            self.head = None
            self.tail = None
        elif self.used == 2:
            self.tail = self.head
            self.tail.next = None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            self.tail = p
            self.tail.next = None
        self.used = self.used - 1
        print("delete after:", self.tail.val, self.used)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.head is None:
            return -1
        return self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.tail is None:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.used == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.used >= self.size


if __name__ == "__main__":
    # Your MyCircularDeque object will be instantiated and called as such:
    circularDeque = MyCircularDeque(85)
    assert circularDeque.insertLast(66)
    assert circularDeque.insertLast(77)
    assert circularDeque.deleteLast()
    assert circularDeque.insertFront(74)
    assert circularDeque.insertFront(77)
    assert circularDeque.getRear() == 66
