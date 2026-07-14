# Brute Force
from typing import List

# class Solution:
#   def has_duplicate(self, nums: List[int]) -> bool:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# s=Solution()
# print(s.has_duplicate(nums=[1,2,3,4]))


# 2. Sorting
# class Solution:
#     def hasDuplicate(self,nums:List[int])->bool:
#         for i in range(0,len(nums)):

#             if nums[i]==nums[i-1]:
#                 return True
#         return False

# s=Solution()
# nums=[1,2,3,4,4]
# nums.sort()
# print(s.hasDuplicate(nums))


# 3 Hash Set


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:  # this for loop  gaves direct values
            if num in seen:
                return True
            seen.add(num)
        return False


s = Solution()
nums = [1, 2, 3, 4, 6]
print(s.hasDuplicate(nums))


# in for loop range used here it gaves indexes
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()

#         for i in range(len(nums)):
#             if nums[i] in seen:
#                 return True

#             seen.add(nums[i])

#         return False
