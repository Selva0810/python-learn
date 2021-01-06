
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        j = 0
        n = len(nums)
        while j < n:

            for i in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [j,i]
                i += 1

            j += 1

        return []




num = [3,2,3]

target = 6
s = Solution()
print(s.twoSum(num,target))

