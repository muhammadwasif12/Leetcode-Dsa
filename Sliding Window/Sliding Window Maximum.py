import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):

        heap = []
        result = []

        for r in range(len(nums)):

            # current element heap mein add
            heapq.heappush(heap, (-nums[r], r))

            # window se bahar elements remove
            while heap[0][1] <= r - k:
                heapq.heappop(heap)

            # jab window size k ho
            if r >= k - 1:
                result.append(-heap[0][0])

        return result
