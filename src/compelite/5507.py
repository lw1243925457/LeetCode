class Solution:
    def __init__(self):
        self._ans = ""

    def modifyString(self, s: str) -> str:
        if s == "":
            return ""
        self._replace(s, "", 0)
        return self._ans

    def _replace(self, s, modify, index):
        # print(modify)
        if index >= len(s):
            self._ans = modify
            return self._ans

        if s[index].isalpha():
            res = self._replace(s, modify + s[index], index + 1)
            if res is not None:
                return res
        else:
            chars = list("qwertyuiopasdfghjklzxcvbnm")
            if index - 1 >= 0 and modify[index - 1] in chars:
                chars.remove(modify[index - 1])
            if index + 1 < len(s) and s[index + 1] in chars:
                chars.remove(s[index + 1])

            for c in chars:
                res = self._replace(s, modify + c, index + 1)
                if res is not None:
                    return res


if __name__ == "__main__":
    print(Solution().modifyString(s="j?qg??b"))
    print(Solution().modifyString(s="??????????????????????????"))
