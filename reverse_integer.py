
'''
 Reverse Integer

Solution
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
'''
from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        """
        Do not return anything, modify s in-place instead.
        """
        rev = 0
        check = 0
        print (x)
        if x < 0:
            print("why")
            check = 1
        n = abs(x)
        while n > 0:
            a = n % 10
            rev = rev * 10 + a
            n = n // 10

        if check == 1:
            rev = rev * -1


        if abs(rev) < 2 ** 31 and rev != 2 ** 31 - 1:
            return rev
        else:
            return 0

s = Solution()


x = 432
print(s.reverse(x))

