
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.insert(len(nums),0)
        return nums


    def moveZeroes1(self, nums: List[int]) -> None:
        c = 0

        for i in range(len(nums)):
            print (f"outside if :{nums[i]}")
            if nums[i]:
                print(f"inside if :{nums[i]}")

                nums[c] = nums[i]
                c += 1

        while c < len(nums):
            nums[c] = 0
            c += 1
        return nums

num = [0, 1, 0, 3, 12]

s = Solution()
print(s.moveZeroes(num))
num = [0, 1, 0, 0, 1, 2, 3, 12]

print(s.moveZeroes1(num))
