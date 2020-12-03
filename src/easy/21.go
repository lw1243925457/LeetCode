//将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
//
//
//
// 示例：
//
// 输入：1->2->4, 1->3->4
//输出：1->1->2->3->4->4
//
// Related Topics 链表
// 👍 1406 👎 0
package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
//  Definition for singly-linked list.
type ListNode struct {
	Val int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}

	ans := &ListNode{}
	p := ans

	for l1 != nil || l2 != nil {
		if l1 == nil || (l2 != nil && l1.Val >= l2.Val) {
			p.Next = &ListNode{l2.Val, nil}
			l2 = l2.Next
		} else {
			p.Next = &ListNode{l1.Val, nil}
			l1 = l1.Next
		}
		p = p.Next
	}

	return ans.Next
}
//leetcode submit region end(Prohibit modification and deletion)

func main() {
	l1 := ListNode{1, &ListNode{2, &ListNode{4, nil}}}
	l2 := ListNode{1, &ListNode{3, &ListNode{4, nil}}}
	res := mergeTwoLists(&l1, &l2)
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}