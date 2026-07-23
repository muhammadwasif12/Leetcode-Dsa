# 1. Encoding & Decoding
from typing import List, defaultdict

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i : i + sz])
            i += sz
        return res


# 1. Encoding & Decoding (optimal)


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res



# Encoded String

# 3#abc5#hello1#x

# ↓

# Read 3

# ↓

# Take next 3 chars

# abc

# ↓

# Read 5

# ↓

# Take next 5 chars

# hello

# ↓

# Read 1

# ↓

# Take next 1 char

# x

# ↓

# ["abc","hello","x"]









# Pehli approach:

# 3,5,1,#abchellox
# Pehle saari lengths store karni padti thi.
# Phir doosri baar strings padhni padti thi.

# Is approach me:

# 3#abc5#hello1#x

# Har string ke saath uski length likhi hui hai.

# Isliye decode karte waqt:

# Length padho.
# Turant utni string read kar lo.
# Agli string par chale jao.

# Yani extra sizes list ki zarurat nahi padti, aur code bhi chhota aur zyada elegant ho jata hai.