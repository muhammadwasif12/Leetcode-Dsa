# Brute Force


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res


#Sliding Window using hash set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])

            res = max(res, r - l + 1)

        return res


s = Solution()

print(s.lengthOfLongestSubstring("zxyzxyz"))  # 3
print(s.lengthOfLongestSubstring("xxxx"))  # 1
print(s.lengthOfLongestSubstring("pwwkew"))  # 3
