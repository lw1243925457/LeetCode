"""
面试题 01.06. 字符串压缩
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。
通过次数4,509提交次数9,010
"""
class Solution:
    def compressString(self, S: str) -> str:
        if len(S) <= 1:
            return S

        beforeChar = None
        count = 0
        result = ""
        for char in S:
            if beforeChar is None:
                beforeChar = char
                count = count + 1
            elif beforeChar == char:
                count = count + 1
            else:
                result = result + beforeChar + str(count)
                beforeChar = char
                count = 1
        result = result + beforeChar + str(count)

        if len(result) >= len(S):
            return S
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.compressString("aabcccccaaa"))
    assert s.compressString("aabcccccaaa") == "a2b1c5a3"
    assert s.compressString("a") == "a"
    assert s.compressString("abc") == "abc"
