from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        # Do XOR of all elements and return
        for i in range(1, n):
            res = res ^ nums[i]

        return res

    def singleNumber1(self, nums: List[int]) -> int:
        while len(nums) > 0:
            x = nums.pop(0)
            try:
                nums.remove(x)
            except:
                return x

s=Solution()
print (s.singleNumber([4,4,1,2,1,2,3]))

print (s.singleNumber1([4,4,1,2,1,2,3]))

        