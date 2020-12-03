package main

import "fmt"

//Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func countNodes(root *TreeNode) int {
	if root == nil {
	    return 0
	}

	return 1 + countNodes(root.Left) + countNodes(root.Right)
}

func main() {
	node := TreeNode{1, nil, nil}
	if countNodes(&node) != 1 {
		fmt.Println("error")
	}

	node.Left := TreeNode{1, nil, nil}
	if countNodes(&node) != 2 {
		fmt.Println("error")
	}

	node.Right := TreeNode{1, nil, nil}
	if countNodes(&node) != 3 {
		fmt.Println("error")
	}

	node.Right.Left := TreeNode{1, nil, nil}
	if countNodes(&node) != 4 {
		fmt.Println("error")
	}
}
