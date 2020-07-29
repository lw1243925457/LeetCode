"""
30. 串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。



示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
通过次数39,505提交次数125,998


解题思路：
1.暴力hash解：
    循环遍历s，将可能的子串存入hash中,s可能存在重复
    枚举words中可能组成的字符串，枚举也可以存在重复
    匹配生成答案

边界条件还是考虑不周全

最后还是借鉴了高手的思路
1方法中的枚举数据量太大了，2^N，这个以后需要注意，万万不能在程序中搞这种
它的用hash表去判断和字符串是否匹配的思路很妙，很值得借鉴

2.三hash解：
    循环遍历s，将可能的子串存入hash中,s可能存在重复
    遍历words存入hash中，记录单词出现的次数
    判断S存在hash中的每个子串是否匹配：当words中的单词全部用上时表示匹配，加入其字符串对应的序号即可
"""
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []

        length = len(words[0])
        size = length * len(words)

        n = len(s)
        print(n, size, s, words)
        if n < size:
            return []

        ans = []
        sHash = {}
        for i in range(0, n-size+1):
            if s[i:i+size] not in sHash:
                sHash[s[i:i+size]] = [i]
            else:
                sHash[s[i:i+size]].append(i)
        print("shash:", sHash)

        wHash = {}
        for word in words:
            if word not in wHash:
                wHash[word] = 1
            else:
                wHash[word] = wHash[word] + 1
        print("whash:", wHash)

        for subs in sHash.keys():
            if self.isMatch(subs, wHash, size, length):
                for index in sHash[subs]:
                    ans.append(index)
        return ans

    def isMatch(self, subs, wHash, size, length):
        wc = {}
        for i in range(0, size, length):
            word = subs[i:i+length]
            if word not in wHash:
                return False
            else:
                if word not in wc:
                    wc[word] = 1
                else:
                    wc[word] = wc[word] + 1

        for key in wHash:
            if key not in wc:
                return False
            if wHash[key] != wc[key]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(solution.findSubstring(s, words))

    s = "foobarfoobar"
    words = ["foo", "bar"]
    print(solution.findSubstring(s, words))

    s= "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
    words = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]
    print(solution.findSubstring(s, words))

