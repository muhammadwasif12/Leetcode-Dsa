from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            if index == len(nums):
                return

            # Include current number
            path.append(nums[index])
            backtrack(index, remaining - nums[index])

            # Undo the choice
            path.pop()

            # Exclude current number
            backtrack(index + 1, remaining)

        backtrack(0, target)
        return result
