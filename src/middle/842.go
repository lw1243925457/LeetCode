package main

import (
	"fmt"
	"math"
)

/*
不能以0开头，但单独一个0可以
数组列表长度大于等于3
F[i] = f[i-1] + f[i-2]
 */
func splitIntoFibonacci(S string) []int {
	var ret []int
	find(S, 0, 0, 0, ret)
	return ret
}

func find(str string, index int, sum int, pre int, ret []int) bool {
	fmt.Println(str, index, sum, pre, ret)
	if index >= len(str) {
		return len(ret) >= 3
	}

	cur := 0
	for i := index; i < len(str); i++ {
		if i > index && str[index] == '0' {
			break
		}

		cur = cur * 10 + int(str[i] - '0')
		if cur > math.MaxInt32 {
			break
		}

		if len(ret) >= 2 {
			if cur < sum {
				continue
			}
			if cur > sum {
				break
			}
		}

		ret = append(ret, cur)
		if find(str, i + 1, pre + cur, cur, ret) {
			return true
		}
		ret = ret[:len(ret) - 1]
	}
	return false
}

func main() {
	fmt.Println(splitIntoFibonacci("123456789"))
}
