from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            res += min(leftMax, rightMax) - height[i]
        return res


s = Solution()
print(s.trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))


# 2 pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

























# Ye **Optimal Two Pointer Solution (O(n), O(1))** hai. Isme **leftMax** aur **rightMax** ko baar baar dhoondna nahi padta. Chalo line by line samajhte hain.

# ---

# # 1.

# ```python
# if not height:
#     return 0
# ```

# Agar array empty hai.

# ```python
# height=[]
# ```

# To water bhi

# ```text
# 0
# ```

# ---

# # 2.

# ```python
# l = 0
# r = len(height)-1
# ```

# Do pointers.

# Example

# ```python
# height=[0,2,0,3,1,0,1,3,2,1]
# ```

# ```text
# l                         r
# ↓                         ↓
# 0 2 0 3 1 0 1 3 2 1
# ```

# ---

# # 3.

# ```python
# leftMax = height[l]
# rightMax = height[r]
# ```

# Initially

# ```python
# leftMax=0
# rightMax=1
# ```

# Ye **ab tak ki sabse badi wall** store karenge.

# ---

# # 4.

# ```python
# res=0
# ```

# Total water.

# ---

# # 5.

# ```python
# while l<r:
# ```

# Jab tak dono pointers mil nahi jate.

# ---

# # Sabse Important Line ⭐

# ```python
# if leftMax < rightMax:
# ```

# Tum puchoge:

# **Sir, leftMax aur rightMax compare hi kyu kar rahe hain?**

# ### Example

# ```text
# LeftMax = 2
# RightMax = 5
# ```

# Diagram

# ```text
# 2              5
# █              █
# █              █
# █      ?       █
# -----------------
# ```

# Water kis se decide hoga?

# Formula yaad hai?

# ```text
# Water = min(leftMax,rightMax)
# ```

# Yahan

# ```python
# min(2,5)=2
# ```

# Matlab chahe right wall 100 bhi ho jaye,

# ```text
# 2              100
# █               █
# █               █
# █       ?       █
# -----------------
# ```

# Water fir bhi

# ```text
# 2
# ```

# tak hi rukega.

# Isliye jab

# ```python
# leftMax < rightMax
# ```

# ho,

# **sirf left side process karni hoti hai.**

# ---

# # 6.

# ```python
# l += 1
# ```

# Left pointer ko aage badhao.

# Example

# Pehle

# ```text
# ↓
# 0 2 0 3 1 0
# ```

# Baad me

# ```text
#   ↓
# 0 2 0 3 1 0
# ```

# ---

# # 7.

# ```python
# leftMax=max(leftMax,height[l])
# ```

# Agar nayi wall badi hai

# to

# leftMax update.

# Example

# Current

# ```python
# leftMax=2
# ```

# New wall

# ```python
# height[l]=3
# ```

# To

# ```python
# leftMax=max(2,3)

# =3
# ```

# ---

# # 8.

# ```python
# res += leftMax-height[l]
# ```

# Ye bahut important hai.

# Example

# ```text
# LeftMax

# 3
# █
# █
# █

# Current Wall

# 1
# █
# ```

# Water

# ```text
# 3-1=2
# ```

# To

# ```python
# res+=2
# ```

# ---

# # Agar

# ```python
# leftMax=3

# height[l]=3
# ```

# Water

# ```python
# 3-3

# 0
# ```

# Kuch add nahi hoga.

# ---

# # Else Part

# Agar

# ```python
# leftMax>=rightMax
# ```

# to

# right side process.

# ---

# ## Pointer

# ```python
# r-=1
# ```

# ---

# ## Update

# ```python
# rightMax=max(rightMax,height[r])
# ```

# Example

# ```python
# rightMax=2

# height[r]=5
# ```

# To

# ```python
# rightMax=5
# ```

# ---

# ## Water

# ```python
# res+=rightMax-height[r]
# ```

# Example

# ```text
# RightMax

# 5
# █
# █
# █
# █
# █

# Current

# 2
# █
# █
# ```

# Water

# ```text
# 5-2

# 3
# ```

# ---

# # Dry Run

# Example

# ```python
# height=[3,0,3]
# ```

# Initially

# ```text
# l=0

# r=2

# leftMax=3

# rightMax=3
# ```

# ---

# ### Iteration 1

# ```python
# leftMax<rightMax
# ```

# No

# Isliye else.

# ```python
# r=1
# ```

# Current

# ```python
# height[1]=0
# ```

# Update

# ```python
# rightMax=max(3,0)

# =3
# ```

# Water

# ```python
# 3-0

# 3
# ```

# ```python
# res=3
# ```

# ---

# ### Iteration 2

# ```python
# r=0
# ```

# Loop end.

# Answer

# ```text
# 3
# ```

# ---

# # Ye Brute Force se fast kyu hai?

# Brute Force me har index ke liye

# ```text
# Left Max search

# +

# Right Max search
# ```

# karte the.

# Isme

# ```text
# Left Max
# ```

# already yaad hai.

# Aur

# ```text
# Right Max
# ```

# already yaad hai.

# Isliye dubara search nahi karni padti.

# ---

# # Golden Rule (Is Question ka)

# ```
# 1. Agar leftMax < rightMax
#    👉 Left pointer move karo.

# 2. Warna
#    👉 Right pointer move karo.

# 3. Water =
#    leftMax - currentHeight
#    ya
#    rightMax - currentHeight
# ```

# ## 💡 Ek line me intuition

# * **Chhoti maximum wall (`leftMax` ya `rightMax`) hi water level decide karti hai.**
# * Agar `leftMax < rightMax` hai, to left side ka water **already fix** hai. Right side future me aur badi ho jaye to bhi `min(leftMax, rightMax)` nahi badlega jab tak `leftMax` chhota hai.
# * Isi wajah se hum sirf **left pointer** move karte hain. Isi tarah agar `rightMax` chhota ho to sirf **right pointer** move karte hain.

# Yehi idea is solution ko **O(n)** bana deta hai.
