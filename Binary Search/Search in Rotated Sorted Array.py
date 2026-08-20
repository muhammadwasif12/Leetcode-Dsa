from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            # Target mil gaya
            if nums[m] == target:
                return m

            # Left side sorted hai
            if nums[l] <= nums[m]:

                # Target left sorted range mein hai
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # Right side sorted hai
            else:

                # Target right sorted range mein hai
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


s = Solution()

print(s.search([3, 4, 5, 6, 1, 2], 1))  # 4
print(s.search([3, 5, 6, 0, 1, 2], 4))  # -1
print(s.search([3, 4, 5, 6, 1, 2], 6))  # 3
