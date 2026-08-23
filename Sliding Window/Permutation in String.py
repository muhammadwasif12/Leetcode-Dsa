class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False


# sliding window


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # s1 ki frequency
        for c in s1:
            count1[ord(c) - ord("a")] += 1

        l = 0

        # s2 par sliding window
        for r in range(len(s2)):

            # right character window mein add
            count2[ord(s2[r]) - ord("a")] += 1

            # window ko s1 ki length ka rakho
            if r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord("a")] -= 1
                l += 1

            # frequencies same hain?
            if count1 == count2:
                return True

        # koi permutation nahi mili
        return False
