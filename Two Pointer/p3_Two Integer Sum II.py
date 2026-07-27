from typing import List
# Brute Force


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            
            for j in range(len(numbers)):
                if i==j:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]


s=Solution()
print(s.twoSum(numbers=[1,2,3,4],target=3))


# 2 pointer


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while(l<r):
         curSum=numbers[l]+numbers[r]
           
         if curSum == target:
            return [l + 1, r + 1]

         if curSum<target:
             l+=1
         if curSum>target:
             r-=1  

        return []       


s=Solution()
print(s.twoSum(numbers=[1,2,3,4],target=3))
