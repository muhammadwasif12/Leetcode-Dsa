from typing import List

# Brute Force

class Solution:
    def findMin(self, nums: List[int]) -> int:

        minimum = nums[0]

        for i in range(len(nums)):

            if nums[i] < minimum:
                minimum = nums[i]

        return minimum


s = Solution()

# print(s.findMin([3, 4, 5, 6, 1, 2]))  # 1
# print(s.findMin([4, 5, 0, 1, 2, 3]))  # 0
# print(s.findMin([4, 5, 6, 7]))  # 4


# Binary Search

class Solution:
    def findMin(self,nums:List[int])->int:
        l=0
        r=len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                res=min(res,nums[l])
                break

            m=(l+r)//2
            res=min(res,nums[m])
            if nums[m] >= nums[l]:
                l=m+1
            else:
                r=m-1
            return res


print(s.findMin([3, 4, 5, 6, 1, 2]))  # 1
print(s.findMin([4, 5, 0, 1, 2, 3]))  # 0
print(s.findMin([4, 5, 6, 7]))  #
