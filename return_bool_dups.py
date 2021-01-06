from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=[]
        for num  in nums:
            if num not in seen:
                seen.append(num)
            else:
                return False
        return True

s=Solution()
print (s.containsDuplicate([1,2,3,1]))


        