# Brute force
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res


s = Solution()
print(s.maxArea(heights=[1, 7, 2, 5, 4, 7, 3, 6]))


# 2 pointer
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)  # r-l=width  #area =hxw
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res


s = Solution()
print(s.maxArea(heights=[1, 7, 2, 5, 4, 7, 3, 6]))
