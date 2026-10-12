import heapq


class MedianFinder:

    def __init__(self):
        self.small = []  # Max Heap (negative numbers)
        self.large = []  # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Small half ka maximum, large half mein bhejo
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Small half ko equal ya 1 element bara rakho
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0
