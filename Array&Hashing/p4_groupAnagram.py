# 1 Soritng
from typing import List, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)          #res["aet"] = []
        for s in strs: 
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)       #res["aet"].append("eat")
        return list(res.values())


s = Solution()
print(s.groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))


# Isliye defaultdict(list) bahut useful hai jab dictionary ki values me list store karni ho.


# sorted(s)   this func return list not sytring  ['a', 'e', 't']

# Ab list ko string banana hai.
# "".join(...)
# "aet"


# 2. Hash Table
#


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: 
            count = [0] * 26        #26 letters ke liye frequency array banayi.
            for c in s:
                count[ord(c) - ord("a")] += 1   #Ye character ko uske index me convert karti hai.
            res[tuple(count)].append(s)          
        return list(res.values())

# 
s = Solution()
print(s.groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))












# Loop chalega

# for c in s:
# First Iteration
# c = "e"

# Ab

# ord("e")

# Result

# 101

# Aur

# ord("a")

# Result

# 97

# Difference

# 101 - 97 = 4

# To

# count[4] += 1

# Ab list

# [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# .....

# [
# 1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0
# ]

# Ye "eat" ka fingerprint (signature) hai.

# Ab ye line

# res[tuple(count)].append(s)

# Pehle

# tuple(count)

# Banega

# (
# 1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0
# )

# Ye dictionary ki key ban jayegi.

# Aur

# append(s)

# Matlab

# append("eat")

# Dictionary

# {
# (freq):
# ["eat"]
# }












# ord()

# ASCII value deta hai.

# ord('a') = 97













# res[tuple(count)].append(s)

# Isko right se left padhna.

# Example

# Maan lo

# s = "eat"

# Aur uska frequency count ban gaya:

# count = [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

# Ab

# tuple(count)

# ban jayega

# (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)

# Ye dictionary ki key hai.

# Ab maan lo abhi dictionary khali hai.

# res = {}

# Lekin defaultdict(list) ki wajah se jab Python dekhega:

# res[tuple(count)]

# Aur key nahi milegi...

# To Python khud bana dega:

# res[tuple(count)] = []

# Ab dictionary ban gayi:

# {
#     (1,0,0,0,1,...): []
# }

# Ab last part:

# .append(s)

# Matlab:

# .append("eat")

# Ab dictionary ho gayi:

# {
#     (1,0,0,0,1,...): ["eat"]
# }
# Ab next word
# s = "tea"

# Iski frequency bhi exactly same hai.

# To tuple(count) bhi same hoga.

# Python dekhega:

# res[tuple(count)]

# Aur is baar key pehle se hai:

# {
#     (1,0,0,0,1,...): ["eat"]
# }

# Ab sirf:

# .append("tea")

# Dictionary:

# {
#     (1,0,0,0,1,...): ["eat", "tea"]
# }
# Ek line me yaad rakho
# res[tuple(count)].append(s)

# ka matlab hai:

# "Jis frequency ki key hai, us group me current string (s) add kar do."










# Dictionary ki key immutable (change na hone wali) honi chahiye.

# Ye valid keys hain:

# "aet"          # string ✅
# 123            # int ✅
# (1,2,3)        # tuple ✅

# Ye valid nahi hain:

# [1,2,3]        # list ❌
# {"a":1}        # dict ❌
# set([1,2])     # set ❌





# Isliye

# count ek list hai.

# count = [1,0,0,1]

# List ko dictionary key nahi bana sakte.

# To usko tuple me convert karte hain:

# tuple(count)

# Ban gaya:

# (1,0,0,1)

# Ab ye dictionary key ban sakta hai.




