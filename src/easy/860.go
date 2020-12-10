package main

import (
	"fmt"
)

/*
先找20,10,5
 */
func lemonadeChange(bills []int) bool {
	fiveNumber := 0
	tenNumber := 0

	for _, bill := range bills {
		if bill == 5 {
			fiveNumber += 1
		} else if bill == 10 {
			fiveNumber -= 1
			tenNumber += 1
		} else {
			if tenNumber == 0 {
				fiveNumber -= 3
			} else {
				fiveNumber -= 1
				tenNumber -= 1
			}
		}

		if fiveNumber < 0 {
			return false
		}

	}
	return true
}

func main() {
	fmt.Println(lemonadeChange([]int{5,5,5,10,20}))
	fmt.Println(lemonadeChange([]int{5,5,10}))
	fmt.Println(lemonadeChange([]int{10,10}))
	fmt.Println(lemonadeChange([]int{5,5,10,10,20}))
}
