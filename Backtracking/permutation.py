from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose number
                path.append(nums[i])
                used[i] = True

                backtrack()

                # Undo choice
                path.pop()
                used[i] = False

        backtrack()
        return result
