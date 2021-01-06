
'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''
from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:

        if len(s) == 1:
            return 0

        uniq = dict()
        for n in s:
            if n in uniq:
                uniq[n] += 1
            else:
                uniq[n] = 1

        print (uniq)
        for k,w in uniq.items():
            if w ==1:
                return s.index(k)
        return -1

    def firstUniqChar1(self, s: str) -> int:
        for x in s:
            if s.count(x) == 1:
                return s.index(x)
        return -1

s = Solution()

s1 = "csdfxcs"
print(s.firstUniqChar(s1))
print(s.firstUniqChar1(s1))


