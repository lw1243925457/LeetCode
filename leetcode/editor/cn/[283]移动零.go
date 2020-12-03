//给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
//
// 示例: 
//
// 输入: [0,1,0,3,12]
//输出: [1,3,12,0,0] 
//
// 说明: 
//
// 
// 必须在原数组上操作，不能拷贝额外的数组。 
// 尽量减少操作次数。 
// 
// Related Topics 数组 双指针 
// 👍 828 👎 0
package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func moveZeroes(nums []int)  {
	begin := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[begin] = nums[begin], nums[i]
			begin += 1
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

