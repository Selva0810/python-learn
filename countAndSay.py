
'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''
from typing import List

from collections import defaultdict

class Solution:

    def countAndSay(self, n: int) -> str:

        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s

    def countAndSay1(self, n: int) -> str:
        res = ['1']

        while n > 1:
            tmp = []
            cnt = 1

            for i in range(1, len(res)):

                if res[i - 1] == res[i]:
                    cnt += 1

                else:
                    tmp.append(str(cnt))
                    tmp.append(res[i - 1])
                    cnt = 1

            tmp.append(str(cnt))
            tmp.append(res[-1])

            n -= 1
            res = tmp

        return ''.join(res)
soln = Solution()

n=6
print(soln.countAndSay(n))

print(soln.countAndSay1(n))
