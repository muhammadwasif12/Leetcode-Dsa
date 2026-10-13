from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return

            # Choice 1: Include current number
            path.append(nums[index])
            backtrack(index + 1)

            # Undo the choice
            path.pop()

            # Choice 2: Exclude current number
            backtrack(index + 1)

        backtrack(0)
        return result
