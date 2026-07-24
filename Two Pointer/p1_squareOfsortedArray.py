from typing import List


# Sorting
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(num * num)

        return sorted(res)


s = Solution()
print(s.sortedSquares(nums=[-4, -1, 0, 3, 10]))


# TWo Pointer
# 3. Two Pointers - II
# Intuition
# This is an optimization of the previous approach that avoids the final reversal step. Instead of building the result from smallest to largest and reversing, we fill the result array from the end to the beginning. We still use two pointers to compare the absolute values at both ends, but we place each square directly in its final position.

# Algorithm
# Create a result array of the same size as the input.
# Initialize l = 0, r = n - 1, and resIndex = n - 1 (pointing to the last position).
# While l <= r:
# Compare the absolute values of nums[l] and nums[r].
# Place the larger square at res[resIndex] and move the corresponding pointer.
# Decrement resIndex.
# Return the result array (no reversal needed).


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        res = [0] * n
        res_index = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[res_index] = nums[l] * nums[l]
                l += 1

            else:
                res[res_index] = nums[r] * nums[r]
                r -= 1
            res_index -= 1

        return res


s = Solution()
print(s.sortedSquares(nums=[-4, -1, 0, 3, 10]))
