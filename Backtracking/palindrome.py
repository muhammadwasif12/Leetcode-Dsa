from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(text):
            return text == text[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                part = s[start : end + 1]

                if not isPalindrome(part):
                    continue

                path.append(part)
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return result
