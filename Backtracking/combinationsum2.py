from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Sorted array: no need to try larger numbers
                if candidates[i] > remaining:
                    break

                # Choose current number
                path.append(candidates[i])

                # Move forward: each element can be used once
                backtrack(i + 1, remaining - candidates[i])

                # Undo choice
                path.pop()

        backtrack(0, target)
        return result
