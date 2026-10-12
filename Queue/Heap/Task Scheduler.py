from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            if heap:
                count = heapq.heappop(heap) + 1

                if count < 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                count, available_time = queue.popleft()
                heapq.heappush(heap, count)

        return time
