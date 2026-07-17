from typing import List

# Array

# class Solution:
#     def isTwoSum(self, nums: List[int], target: int) -> bool:

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#    return []

# s = Solution()
# print(s.isTwoSum(nums=[1, 2, 3, 4,6,7,4,8,9], target=9))


# HashMap(One Pass)
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = {}
        for i in range(len(nums)):

            r = target - nums[i]
            if r in result:  # Python keys me check karega.
                return [result[r], i]

            result[nums[i]] = i


s1 = Solution()
print(s1.twoSum(nums=[1, 2, 3, 5], target=5))


# Agar tum value me check karna chahte ho
# r in result.values()
