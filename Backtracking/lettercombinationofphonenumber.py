from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        path = ""

        def backtrack(index):
            if index == len(digits):
                result.append(path)
                return

            letters = phone[digits[index]]

            for letter in letters:
                backtrack_helper(letter, index)

        def backtrack_helper(letter, index):
            nonlocal path
            old_path = path
            path = old_path + letter
            backtrack(index + 1)
            path = old_path

        backtrack(0)
        return result
