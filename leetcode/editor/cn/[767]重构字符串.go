//给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。 
//
// 若可行，输出任意可行的结果。若不可行，返回空字符串。 
//
// 示例 1: 
//
// 
//输入: S = "aab"
//输出: "aba"
// 
//
// 示例 2: 
//
// 
//输入: S = "aaab"
//输出: ""
// 
//
// 注意: 
//
// 
// S 只包含小写字母并且长度在[1, 500]区间内。 
// 
// Related Topics 堆 贪心算法 排序 字符串 
// 👍 194 👎 0
package main

import (
	"container/heap"
	"sort"
)

//leetcode submit region begin(Prohibit modification and deletion)
var cnt [26]int

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool  { return cnt[h.IntSlice[i]] > cnt[h.IntSlice[j]] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{}   { a := h.IntSlice; v := a[len(a)-1]; h.IntSlice = a[:len(a)-1]; return v }
func (h *hp) push(v int)         { heap.Push(h, v) }
func (h *hp) pop() int           { return heap.Pop(h).(int) }

func reorganizeString(s string) string {
	n := len(s)
	if n <= 1 {
		return s
	}

	cnt = [26]int{}
	maxCnt := 0
	for _, ch := range s {
		ch -= 'a'
		cnt[ch]++
		if cnt[ch] > maxCnt {
			maxCnt = cnt[ch]
		}
	}
	if maxCnt > (n+1)/2 {
		return ""
	}

	h := &hp{}
	for i, c := range cnt[:] {
		if c > 0 {
			h.IntSlice = append(h.IntSlice, i)
		}
	}
	heap.Init(h)

	ans := make([]byte, 0, n)
	for len(h.IntSlice) > 1 {
		i, j := h.pop(), h.pop()
		ans = append(ans, byte('a'+i), byte('a'+j))
		if cnt[i]--; cnt[i] > 0 {
			h.push(i)
		}
		if cnt[j]--; cnt[j] > 0 {
			h.push(j)
		}
	}
	if len(h.IntSlice) > 0 {
		ans = append(ans, byte('a'+h.IntSlice[0]))
	}
	return string(ans)
}

//leetcode submit region end(Prohibit modification and deletion)
