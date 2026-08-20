from typing import List


#Brute force
class Solution:
    def searchMatrix(self,matrix:List[List[int]],target:int)->bool:
        for i in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[i][c]==target:
                    return True

        return False

s=Solution()   
print(s.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))





#Binary searcch
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Row search
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:

            row = (top + bottom) // 2

            # Target is row ke range mein hai
            if matrix[row][0] <= target <= matrix[row][-1]:
                break

            # Target right side ki rows mein hai
            elif target > matrix[row][-1]:
                top = row + 1

            # Target left side ki rows mein hai
            else:
                bottom = row - 1

        else:
            return False

        # Ab selected row mein binary search
        left = 0

        right = len(matrix[row]) - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif target > matrix[row][mid]:
                left = mid + 1

            else:
                right = mid - 1

        return False


s = Solution()

print(s.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))

print(s.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15))