'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

    k %= len(nums)
    print(f"k={k}")
    reverse(nums, 0, len(nums))

    reverse(nums, 0, k)

    reverse(nums, k, len(nums))

    print(nums)


class Solution:

    def rotate1(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        print(nums)

    def rotate2(self, nums, k):
        count = 0
        start = 0
        while count < len(nums):
            curr = start
            prev = nums[curr]
            while True:
                idx = (curr + k) % len(nums)
                nums[idx], prev = prev, nums[idx]
                curr = idx
                count += 1
                if start == curr:
                    break
            start += 1


s = Solution()
rotate([1, 2, 3, 4, 5, 6, 7], k=3)
s.rotate1([1, 2, 3, 4, 5, 6, 7], k=3)

s.rotate2([1, 2, 3, 4, 5, 6, 7], k=3)
