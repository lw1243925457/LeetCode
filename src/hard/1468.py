"""
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        找到最高值
        作为另一种解决方案，请从每个长方形的角度来考虑。每个长方形上面都有水。每个长方形上面会有多少水？
        每个长方形的顶部都有水，水的高度应与左侧最高长方形和右侧最高长方形的较小值相匹配，也就是说，water_on_top[i] = min(tallest_ bar(0->i), tallest_bar(i, n))。

        找到最高的长方形,把数据分为左右两部分
        分别对左右两个部分进行遍历,使用上面提示的方法计算出面积
        :param heights:
        :return:
        """
        if len(heights) == 0:
            return 0

        hmax = 0
        for num in heights:
            if num > hmax:
                hmax = num

        rh = {"value": hmax}
        for i in range(0, len(heights)):
            if heights[i] == hmax:
                rh["index"] = i
                break

        area = 0
        lh = {"value": heights[0], "index": 0}
        for i in range(0, rh["index"]):
            value = heights[i]
            if value >= lh["value"] or value >= rh["value"]:
                lh["value"] = value
                lh["index"] = i
            elif value < lh["value"] and value < rh["value"]:
                area = area + (min(rh["value"], lh["value"]) - value)

        lh = {"value": heights[len(heights) - 1], "index": len(heights) - 1}
        for i in range(len(heights) - 1, rh["index"], -1):
            value = heights[i]
            if value >= lh["value"] or value >= rh["value"]:
                lh["value"] = value
                lh["index"] = i
            elif value < lh["value"] and value < rh["value"]:
                area = area + (min(rh["value"], lh["value"]) - value)

        return area


if __name__ == "__main__":
    s = Solution()

    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = s.trap(heights)
    assert result == 6

    heights = [5, 4, 1, 2]
    assert s.trap(heights) == 1
