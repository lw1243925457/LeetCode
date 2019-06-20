#!/usr/bin/env python
# @Time    : 2019/6/20 9:00
# @Author  : LiuWei
# @Site    : 
# @File    : 804.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
804. Unique Morse Code Words
Easy

434

363

Favorite

Share
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

Runtime: 32 ms, faster than 97.27% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.2 MB, less than 58.51% of Python3 online submissions for Unique Morse Code Words.
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morseCodeMap = {}
        index = 0
        for char in range(ord("a"), ord("z") + 1):
            print(chr(char))
            morseCodeMap[chr(char)] = morseCode[index]
            index = index + 1
        print(morseCodeMap)

        morseSet = set()
        for word in words:
            morseString = ""
            for char in word:
                morseString += morseCodeMap[char]
            morseSet.add(morseString)
        print(morseSet)
        return len(morseSet)


if __name__ == "__main__":
    solution = Solution()
    words = ["gin", "zen", "gig", "msg"]
    assert solution.uniqueMorseRepresentations(words) == 2