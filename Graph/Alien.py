from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}

        for i, char in enumerate(order):
            rank[char] = i

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if rank[first[j]] > rank[second[j]]:
                        return False
                    break

            else:
                if len(first) > len(second):
                    return False

        return True
