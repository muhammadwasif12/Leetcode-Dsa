class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


s = Solution()
print(s.search(nums=[-1, 0, 2, 4, 6, 8], target=4))


# By Binary Search:


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = (begin + end) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                begin = mid + 1
            elif target < nums[mid]:
                end = mid - 1

        return -1


s = Solution()
print(s.search(nums=[-1, 0, 2, 4, 6, 8], target=8))
