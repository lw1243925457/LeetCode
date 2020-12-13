package main

import "fmt"

/*
谁多谁就赢
一样多，谁在前面谁就赢
 */
func predictPartyVictory(senate string) string {
	RadiantAmount := 0
	DireAmount := 0
	var mans []int32

	for _, c := range senate {
		if c == 'D' {
			DireAmount += 1
		} else {
			RadiantAmount += 1
		}
		mans = append(mans, c)
	}

	index := 0
	for true {
		if senate[index] == 'D' {
			if !kill(&mans, 'R') {
				return "Dire"
			}
		} else if senate[index] == 'R' {
			if !kill(&mans, 'D') {
				return "Radiant"
			}
		}

		fmt.Println(index, mans)
		index += 1
		if index >= len(senate) {
			index = 0
		}
	}
	return ""
}

func kill(mans *[]int32, i int32) bool {
	for index, c := range *mans {
		if c == i {
			(*mans)[index] = 'X'
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(predictPartyVictory("DDRRR"))
}