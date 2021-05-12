'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the
array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        for i in range(N - 1, -1, -1):
            print(f"N - 1:{i}, for:{digits[i]}")
            if digits[i] < 9:
                digits[i] += 1
                print(f"digits[i]:{digits[i]}")
                return digits
            digits[i] = 0

        new_number = [0] * (N + 1)
        print (f"newnumber:{new_number}")
        new_number[0] = 1
        return new_number

num=[9,9,9]
s = Solution()
print (s.plusOne(num))