import heapq

from typing import List
from typing import Interval

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        rooms = []

        for meeting in intervals:
            if rooms and rooms[0] <= meeting.start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, meeting.end)

        return len(rooms)
