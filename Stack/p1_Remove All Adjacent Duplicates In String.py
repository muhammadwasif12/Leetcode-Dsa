class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


s = Solution()

print(s.removeDuplicates("abbaca"))  # ca
print(s.removeDuplicates("azxxzy"))  # ay
print(s.removeDuplicates("aabb"))  # ""
print(s.removeDuplicates("abba"))  # ""


class Solution:

    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            # Agar stack empty hai
            if stack == []:
                stack.append(c)
            # Agar top aur current same hain
            elif stack[-1] == c:
                stack.pop()

            else:
                stack.append(c)

        res = ""
        for ch in stack:
            res += ch

        return res


s = Solution()


print(s.removeDuplicates("abbaca"))  # ca
print(s.removeDuplicates("azxxzy"))  # ay
print(s.removeDuplicates("aabb"))  # ""
print(s.removeDuplicates("abba"))  # ""
