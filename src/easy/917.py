"""
917. 仅仅反转字母
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。



示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"


提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S 中不包含 \ or "
通过次数14,810提交次数26,648
"""
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        result = list(S)
        l = 0
        r = len(result) - 1
        while l < r:
            la = self.isChar(l, result)
            ra = self.isChar(r, result)
            if la and ra:
                temp = result[l]
                result[l] = result[r]
                result[r] = temp
                l = l + 1
                r = r - 1
            elif la and not ra:
                r = r - 1
            elif not la and ra:
                l = l + 1
            elif not la and not ra:
                l = l + 1
                r = r - 1
        print(''.join(result))
        return ''.join(result)

    def isChar(self, index, s):
        cs = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        return cs.find(s[index]) > -1


if __name__ == "__main__":
    s = Solution()
    assert s.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"