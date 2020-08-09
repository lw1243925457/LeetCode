"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]


解题思路：
递归四次，生成可能的字符串
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        length = len(s)

        def convert(nums, index, level, ip):
            if level == 5 and index == length:
                ans.append(ip[:-1])
                return
            if level == 5 and index != length-1:
                return

            for i in range(1, 4):
                if index + i > length:
                    continue
                if i > 1 and nums[index] == "0":
                    continue
                if int(nums[index:index+i]) <= 255:
                    convert(nums, index+i, level+1, ip+nums[index:index+i]+".")

        convert(s, 0, 1, "")
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("010010"))