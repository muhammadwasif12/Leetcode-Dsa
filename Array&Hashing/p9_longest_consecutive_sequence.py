from typing import List


# Sorting Approach (O(n log n))
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = sorted(set(nums))  # Sort + remove duplicates

        longest = 1
        count = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1

            longest = max(longest, count)

        return longest


s = Solution()
print(s.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))


# HashSet  O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for num in numSet:

            # Sequence ka start hai?
            if num - 1 not in numSet:

                length = 1

                while num + length in numSet:
                    length += 1

                longest = max(longest, length)

        return longest


s = Solution()
print(s.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
