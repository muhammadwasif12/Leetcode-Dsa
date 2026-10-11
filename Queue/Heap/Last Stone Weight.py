import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Convert to Max Heap using negative values
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            # Get two heaviest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # If weights are different, push remaining weight
            if first != second:
                remaining = first - second
                heapq.heappush(stones, -remaining)

        # Return last stone's weight, or 0
        return -stones[0] if stones else 0
