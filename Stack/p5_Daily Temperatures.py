from typing import List

# brute - force
from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        result = [0] * len(temp)

        for i in range(len(temp)):

            for j in range(i + 1, len(temp)):

                if temp[j] > temp[i]:
                    result[i] = j - i
                    break

        return result


s = Solution()

print(s.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))


# Stack
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []  # [temperature, index]

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                oldTemp, oldIndex = stack.pop()

                result[oldIndex] = i - oldIndex

            stack.append((temp, i))

        return result


s = Solution()

print(s.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))
