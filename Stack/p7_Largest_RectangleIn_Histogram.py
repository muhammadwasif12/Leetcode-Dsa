from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:

        # Array ki length
        n = len(heights)

        # Abhi tak ka maximum area
        maxArea = 0

        # Stack mein indexes store honge
        # Stack increasing height order maintain karega
        stack = []

        # n + 1 isliye, taake end mein remaining bars bhi process ho jayein
        for i in range(n + 1):

            # Agar stack empty nahi hai
            # AND
            # current bar stack ke top wali bar se chhoti/equal hai
            #
            # to stack wali bar ka rectangle yahin stop ho raha hai
            while stack and (i == n or heights[stack[-1]] >= heights[i]):

                # Stack se index nikalo
                # aur us index ki height nikalo
                height = heights[stack.pop()]

                # Agar stack empty ho gaya:
                #     width = i
                #
                # Agar stack mein kuch bacha hai:
                #     width = current index - previous smaller index - 1
                width = i if not stack else i - stack[-1] - 1

                # Rectangle ka area
                # area = height × width
                maxArea = max(maxArea, height * width)

            # Current index ko stack mein add karo
            stack.append(i)

        # Sabse bada rectangle return karo
        return maxArea


# Object create
s = Solution()


# Test 1
print(s.largestRectangleArea([7, 1, 7, 2, 2, 4]))

# Test 2
print(s.largestRectangleArea([1, 3, 7]))

# Test 3
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
