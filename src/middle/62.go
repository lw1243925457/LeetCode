package main

import "fmt"

func uniquePaths(m, n int) int {
	grid := make([][]int, m)
	for i := 0; i < m; i++ {
		grid[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				grid[0][0] = 1
				continue
			}
			if i == 0 {
				grid[i][j] = grid[i][j - 1]
				continue
			}
			if j == 0 {
				grid[i][j] = grid[i - 1][j]
				continue
			}
			grid[i][j] = grid[i-1][j] + grid[i][j-1]
		}
	}
	return grid[m-1][n-1]
}

func main() {
	fmt.Println(uniquePaths(3, 7))
}
