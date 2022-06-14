"""
242. Valid Anagram
Easy

5153

218

Add to List

Share
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s: str, t: str) -> bool:
    d = {}
    for i in s :
        if i in d:
            d[i] += 1
        else:
            d[i] = 1


    for i in t:
        if i in d:
            if d[i]>0:
                d[i] -= 1
            else:
                return False
        else:
            return False
    return True


s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
print(isAnagram(s,t))