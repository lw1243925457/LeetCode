//Given an array nums, write a function to move all 0's to the end of it while m
//aintaining the relative order of the non-zero elements. 
//
// Example: 
//
// 
//Input: [0,1,0,3,12]
//Output: [1,3,12,0,0] 
//
// Note: 
//
// 
// You must do this in-place without making a copy of the array. 
// Minimize the total number of operations. 
// Related Topics Array Two Pointers 
// 👍 4559 👎 144
package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func moveZeroes(nums []int)  {
	tail := len(nums) - 1
	head := 0

	for head <= tail {
		if nums[head] == 0 {
			nums[head], nums[tail] = nums[tail], nums[head]
			tail -= 1
		} else {
			head += 1
		}
	}
}
//leetcode submit region end(Prohibit modification and deletion)

func main() {
	nums := []int {0, 1, 0, 3, 12}
	except := []int {1, 3, 12, 0, 0}
	moveZeroes(nums)

	for i := 0; i < len(nums); i++ {
		if nums[i] != except[i] {
			fmt.Println("err", nums, except)
			break
		}
	}
}
