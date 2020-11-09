//我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。 
//
// （这里，平面上两点之间的距离是欧几里德距离。） 
//
// 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。 
//
// 
//
// 示例 1： 
//
// 输入：points = [[1,3],[-2,2]], K = 1
//输出：[[-2,2]]
//解释： 
//(1, 3) 和原点之间的距离为 sqrt(10)，
//(-2, 2) 和原点之间的距离为 sqrt(8)，
//由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
//我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
// 
//
// 示例 2： 
//
// 输入：points = [[3,3],[5,-1],[-2,4]], K = 2
//输出：[[3,3],[-2,4]]
//（答案 [[-2,4],[3,3]] 也会被接受。）
// 
//
// 
//
// 提示： 
//
// 
// 1 <= K <= points.length <= 10000 
// -10000 < points[i][0] < 10000 
// -10000 < points[i][1] < 10000 
// 
// Related Topics 堆 排序 分治算法 
// 👍 173 👎 0
package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func kClosest(points [][]int, K int) [][]int {
	//return merge(points, K)
	if len(points) <= K {
		return points
	}
	quickSelect(points, K, 0, len(points) - 1)
	return points[:K]
}

func quickSelect(points [][]int, k int, begin int, end int)  {
	selectDistance := distance(points[begin])
	l, r := begin, end

	for l <= r {
		if distance(points[l]) <= selectDistance {
			l += 1
			continue
		}
		if distance(points[r]) > selectDistance {
			r -= 1
			continue
		}

		points[l], points[r] = points[r], points[l]
		l += 1
		r -= 1
	}
	points[begin], points[r] = points[r], points[begin]

	if r == k {
		return
	} else if r < k {
		quickSelect(points, k, r + 1, end)
	} else {
		quickSelect(points, k, begin, r - 1)
	}
}

func merge(points [][]int, K int) [][]int {
	size := len(points)
	if size <= 1 {
		return points
	}

	mid := int(size / 2)
	leftPoints := kClosest(points[0:mid], K)
	rightPoints := kClosest(points[mid:size], K)
	leftSize := len(leftPoints)
	rightSize := len(rightPoints)
	leftIndex := 0
	rightIndex := 0

	ans := [][]int{}

	for K > 0 {
		if leftIndex >= leftSize && rightIndex >= rightSize { break }
		if leftIndex >= leftSize {
			ans = append(ans, rightPoints[rightIndex])
			rightIndex += 1
		} else if rightIndex >= rightSize {
			ans = append(ans, leftPoints[leftIndex])
			leftIndex += 1
		} else if distance(leftPoints[leftIndex]) < distance(rightPoints[rightIndex]) {
			ans = append(ans, leftPoints[leftIndex])
			leftIndex += 1
		} else {
			ans = append(ans, rightPoints[rightIndex])
			rightIndex += 1
		}
		K -= 1
	}

	return ans
}

func distance(point []int) int {
	return point[0] * point[0] + point[1] * point[1]
}
//leetcode submit region end(Prohibit modification and deletion)
