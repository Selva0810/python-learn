'''
Intersection of Two Arrays II

Solution
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for a in nums1:
            if a in nums2:
                res.append(a)
                nums2.remove(a)
                # print(f"nums1:{nums1}")
                # print(f"nums2:{nums2}")

        return res

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        intersection = []
        for i in range(len(nums1)):
            if nums1[i] in hash_map.keys():
                hash_map[nums1[i]] += 1
            else:
                hash_map.update({nums1[i]: 1})
        print(hash_map)
        for i in range(len(nums2)):
            if nums2[i] in hash_map.keys():
                intersection.append(nums2[i])
                hash_map[nums2[i]] -= 1
                if hash_map[nums2[i]] == 0:
                    del hash_map[nums2[i]]

        return intersection

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

nums1 = [1,2,3,1,3]
nums2 = [3,2,2,1,3,3]
s=Solution()
print (s.intersect(nums1,nums2))

print (s.intersect1(nums1,nums2))

print (s.intersect2(nums1,nums2))
