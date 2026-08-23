# Brute Force
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res


# Sliding Window code

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):

            # Agar selling price buying price se zyada hai
            if prices[right] > prices[left]:

                profit = prices[right] - prices[left]

                maxProfit = max(maxProfit, profit)

            else:
                # Naya cheaper buying point mil gaya
                left = right

            # Window ko right side expand karo
            right += 1

        return maxProfit


s = Solution()

print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(s.maxProfit([7, 6, 4, 3, 1]))  # 0
