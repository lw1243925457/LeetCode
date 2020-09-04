def _sortWord(word):
    # print(word)
    for i in range(0, len(word)):
        if not word[i].isalpha():
            continue
        minIndex = i
        for j in range(i+1, len(word)):
            if not word[j].isalpha():
                continue
            if word[j].lower() < word[minIndex].lower():
                minIndex = j
        word[i], word[minIndex] = word[minIndex], word[i]
        # print("".join(word), minIndex)
    return "".join(word)


def sortedStrings(s: str) -> str:
    """
    解题思路：
    1.英文字符排序
    2.非英文字符原地不动
    By?e -> Be?y
    """
    ans = []
    for item in s.split(" "):
        ans.append(_sortWord(list(item)))
    print(" ".join(ans))
    return " ".join(ans)


if __name__ == "__main__":
    # print(sortedStrings("A Famous Saying: Much Ado About Nothing (2012/8)."))
    print("corrent:", "#$A^!#ab&~#CccCCCcDdef&Fff%g@(hIkl@LM^mmOPP((p$P-Rs&T-t$t%Uuv)wxYy@y-yZ")
    assert sortedStrings("#$Y^!#Pf&~#FUyTtAfZhCs&Dly%M@(muOI@Le^mydvc((w$x-cP&t-f$R%CCp)bCck@P-ag") == "#$A^!#ab&~#CccCCCcDdef&Fff%g@(hIkl@LM^mmOPP((p$P-Rs&T-t$t%Uuv)wxYy@y-yZ"