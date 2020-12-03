package main

import (
	"fmt"
	"testing"
)

func removeDuplicates(nums []int) int  {
	if len(nums) == 0 {
		return 0
	}

	ans := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			continue
		}
		nums[ans] = nums[i]
		ans += 1
	}
	return ans
}

func Test(t *testing.T) {
	nums := []int{1, 1, 2}
	if removeDuplicates(nums) != 2 {
		t.Errorf("Error")
	}
	fmt.Println(nums)

	nums = []int{0,0,1,1,1,2,2,3,3,4}
	res := removeDuplicates(nums)
	fmt.Println(res)
	fmt.Println(nums)
}
