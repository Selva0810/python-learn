'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
'''
from typing import List

from collections import defaultdict

import string

print(string.ascii_letters)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s:
            d1[i] += 1

        for j in t:
            d2[j] += 1

        print(d1, d2)
        for k, w in d1.items():
            if k in d2:
                if d1[k] != d2[k]:
                    return False
            else:
                return False
        return True

    def isAnagram1(self, s: str, t: str) -> bool:

        return all(s.count(c) == t.count(c) for c in "abcdefghijklmnopqrstuvwxyz")

    def isAnagram2(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        for c in set(s[:]):
            if t.count(c) != s.count(c):
                return False

        return True


soln = Solution()

s = "anagram"
t = "nagaram"
print(soln.isAnagram(s, t))

print(soln.isAnagram1(s, t))

print(soln.isAnagram2(s, t))
