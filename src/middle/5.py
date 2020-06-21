"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
通过次数295,801提交次数961,380

LeetCode 题解 | 5. 最长回文子串：https://zhuanlan.zhihu.com/p/38251499
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return self.violence(s)
        # return self.improve1(s)
        return self.centerExtend(s)

    def centerExtend(self, s: str) -> str:
        """
        网上的中心扩散法
        :param s:
        :return:
        """
        if len(s) < 2:
            return s
        left = 0
        right = 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len3 = max(len1, len2)
            if len3 > right - left:
                left = i - int((len3 - 1) / 2)
                right = i + int(len3 / 2)
        print(left, right+1)
        return s[left:right+1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
        return r - l - 1

    def violence(self, s: str) -> str:
        """
        初始方法：
        两层直接遍历判断，更新最大长度
        """
        if len(s) == 0:
            return s
        if len(s) == 1:
            return s

        length = 0
        result = s[0]
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                if self.isPalindrome(s[i:j + 1]) > length:
                    length = j - i + 1
                    result = s[i:j + 1]

        print(result)
        return result

    def improve1(self, s: str) -> str:
        """
        初始方法：
        两层直接遍历判断，更新最大长度
        改进1，从后往前遍历，如果字符串长度小于最大的回文长度，则直接放弃回文判断
        """
        if len(s) == 0:
            return s
        if len(s) == 1:
            return s

        length = 0
        result = s[0]
        for i in range(0, len(s)):
            for j in range(len(s)-1, 0, -1):
                if j - i + 1 <= length:
                    continue
                if self.isPalindrome(s[i:j + 1]) > length:
                    print("judge")
                    length = j - i + 1
                    result = s[i:j + 1]

        print(length, result)
        return result

    def isPalindrome(self, s: str) -> int:
        begin = 0
        end = len(s) - 1
        print("str length:", len(s))
        while begin < end:
            if s[begin] != s[end]:
                print("no:", begin, end, s[begin], s[end])
                return 0
            begin = begin + 1
            end = end - 1
            print(begin, end)
        return len(s)


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") == "bab" or s.longestPalindrome("babad") == "aba"
    assert s.longestPalindrome("cbb") == "bb"
    param = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
    assert s.longestPalindrome(param) == "qahaq"
    param = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    s.longestPalindrome(param)
    param = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s.longestPalindrome(param)
