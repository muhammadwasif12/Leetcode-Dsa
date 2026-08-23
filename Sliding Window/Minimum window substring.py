class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""

        countT = {}
        window = {}

        # t ki frequency
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0
        need = len(countT)

        l = 0

        res = ""
        resLen = float("inf")

        for r in range(len(s)):

            # right character window mein add
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # required frequency complete hui?
            if c in countT and window[c] == countT[c]:
                have += 1

            # window valid hai
            while have == need:

                # kya current window shortest hai?
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]

                # left character remove
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return res
