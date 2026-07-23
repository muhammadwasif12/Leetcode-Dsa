from typing import List

# 1. Brute Force


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):

                if i == j:
                    continue
                prod = prod * nums[j]

            res[i] = prod

        return res


s = Solution()
print(s.productExceptSelf(nums=[1, 2, 4, 6]))


# 4. Prefix & Suffix (Optimal)

class Solution:
    def productExceptSelf1(self,nums:List[int])->List[int]:
        prefix=1
        res=[1]*len(nums)

        for i in range(len(nums)):
            res[i]=prefix     #res me wohi value jaye ge jo prefix pr aye ge after mul from left
            prefix *=nums[i]      #prefix value update hoge
            # res[1,1,2,8]  prefix finish
            postfix=1 
        for i in range(len(nums)-1,-1,-1):    #reverse loop range(start,stop,decrement)
            res[i]*=postfix                #res me wohi vaue jaye ge jo postfix me hoge but from w=right side with mul
            postfix *=nums[i]                      #postfix value updte
            # res[48,24,12,8]  postfix

        return res   

s = Solution()
print(s.productExceptSelf1(nums=[1, 2, 4, 6]))
