'''
Given a sorted array nums, remove the duplicates in-place such that each element appears
only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        print(nums)
        return len_


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
print(s.removeDuplicates(nums))
