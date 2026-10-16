import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [-1] * len(queries)

        heap = []
        i = 0

        for q, original_index in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[original_index] = heap[0][0]

        return result
