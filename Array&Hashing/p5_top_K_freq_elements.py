from typing import List, defaultdict

# Sorting:


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


# Bucket SORT

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


class Solution:
    def topkfreq(self,nums:List[int],k:List[int])->List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)

        for num,cnt in count.items():
            freq[cnt].append(num)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res


s=Solution()
print(s.topkfreq(nums=[1, 1, 1, 2, 3, 2], k=2))






class Solution:
    def topkfreqq(self,nums:List[int],k:List[int])->List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num]=1+ count.get(num,0)


        for num,cnt in count.items():
            freq[cnt]=num


        res=[]

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
            if k==len(res):
                return res




