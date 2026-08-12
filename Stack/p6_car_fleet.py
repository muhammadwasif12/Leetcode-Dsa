from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        # Aage wali car pehle
        cars.sort(reverse=True)

        stack = []

        for position, time in cars:

            # Agar peeche wali car same ya kam time mein
            # target tak pahunch sakti hai,
            # to woh aage wali fleet ko catch kar legi.
            if stack and time <= stack[-1]:
                continue

            # New fleet
            stack.append(time)

        return len(stack)


s = Solution()

print(s.carFleet(target=10, position=[1, 4], speed=[3, 2]))

print(s.carFleet(target=10, position=[4, 1, 0, 7], speed=[2, 2, 1, 1]))
