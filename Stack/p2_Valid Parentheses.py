# 1. Brute Force


class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""

s=Solution()
print(s.isValid(s="([{}])"))


# Stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False




















# Dono solutions same problem solve karte hain, lekin approach alag hai.

# ---

# # Problem

# Input:

# ```python
# s = "([{}])"
# ```

# Hame check karna hai ki brackets sahi close ho rahe hain ya nahi.

# Valid examples:

# ```text
# ()
# [] 
# {}
# ([]){}
# ([{}])
# ```

# Invalid examples:

# ```text
# (]
# ([)]
# ((
# ))
# ```

# ---

# # 1) Brute Force

# ```python
# while "()" in s or "{}" in s or "[]" in s:
# ```

# ## Matlab

# Jab tak string me

# ```text
# ()
# ya
# {}
# ya
# []
# ```

# maujood hain,

# tab tak loop chalao.

# ---

# ### Example

# ```python
# s = "([{}])"
# ```

# String

# ```text
# ([{}])
# ```

# Andar

# ```text
# {}
# ```

# hai.

# Loop chalega.

# ---

# ## Step 1

# ```python
# s = s.replace("{}", "")
# ```

# Replace

# ```text
# ([{}])
# ```

# ↓

# ```text
# ([])
# ```

# ---

# Ab string

# ```text
# ([])
# ```

# ---

# Loop dobara.

# Isme

# ```text
# []
# ```

# hai.

# Replace.

# ```python
# s = s.replace("[]", "")
# ```

# Result

# ```text
# ()
# ```

# ---

# Loop dobara.

# ```text
# ()
# ```

# hai.

# Replace.

# ```python
# s = s.replace("()", "")
# ```

# Result

# ```text
# ""
# ```

# ---

# Ab

# ```python
# while "()" in s or "{}" in s or "[]" in s:
# ```

# False.

# Loop khatam.

# ---

# Last line

# ```python
# return s == ""
# ```

# Matlab

# ```python
# return "" == ""
# ```

# Answer

# ```python
# True
# ```

# ---

# ## Invalid Example

# ```python
# s="([)]"
# ```

# String

# ```text
# ([)]
# ```

# Isme

# ```text
# ()
# ```

# nahi.

# ```text
# []
# ```

# nahi.

# ```text
# {}
# ```

# nahi.

# Loop ek baar bhi nahi chalega.

# End me

# ```python
# return s==""
# ```

# Matlab

# ```python
# return "([)]"==""
# ```

# False

# ---

# ## Time Complexity

# Har baar replace hota hai.

# Worst

# ```text
# O(n²)
# ```

# ---

# # 2) Stack Solution

# ```python
# stack = []
# ```

# Empty stack.

# ---

# ## Dictionary

# ```python
# closeToOpen = {
#     ")":"(",
#     "]":"[",
#     "}":"{"
# }
# ```

# Iska matlab

# Agar

# ```text
# )
# ```

# mila

# to uske pehle

# ```text
# (
# ```

# hona chahiye.

# ---

# ## Loop

# ```python
# for c in s:
# ```

# Ek ek character uthao.

# ---

# # Dry Run

# Input

# ```python
# s="([{}])"
# ```

# ---

# ### Character

# ```text
# (
# ```

# Ye closing bracket nahi.

# To

# ```python
# stack.append(c)
# ```

# Stack

# ```text
# (
# ```

# ---

# ### Character

# ```text
# [
# ```

# Push

# Stack

# ```text
# (
# [
# ```

# ---

# ### Character

# ```text
# {
# ```

# Push

# Stack

# ```text
# (
# [
# {
# ```

# ---

# ### Character

# ```text
# }
# ```

# Ab

# ```python
# if c in closeToOpen
# ```

# True.

# ---

# Dictionary

# ```python
# closeToOpen["}"]
# ```

# Answer

# ```text
# {
# ```

# Ab check

# ```python
# stack[-1]
# ```

# Top

# ```text
# {
# ```

# Equal?

# Yes.

# To

# ```python
# stack.pop()
# ```

# Stack

# ```text
# (
# [
# ```

# ---

# ### Character

# ```text
# ]
# ```

# Dictionary

# ```python
# closeToOpen[']']
# ```

# Answer

# ```text
# [
# ```

# Top

# ```text
# [
# ```

# Equal.

# Pop.

# Stack

# ```text
# (
# ```

# ---

# ### Character

# ```text
# )
# ```

# Dictionary

# ```python
# closeToOpen[')']
# ```

# Answer

# ```text
# (
# ```

# Top

# ```text
# (
# ```

# Pop.

# Stack

# ```text
# []
# ```

# ---

# Loop khatam.

# Last line

# ```python
# return True if not stack else False
# ```

# Stack empty.

# Answer

# ```python
# True
# ```

# ---

# # Invalid Example

# ```python
# s="([)]"
# ```

# ### Read (

# Stack

# ```text
# (
# ```

# ---

# ### Read [

# Stack

# ```text
# (
# [
# ```

# ---

# ### Read )

# Dictionary

# ```text
# )
# → (
# ```

# Lekin

# Top

# ```text
# [
# ```

# Match?

# No.

# To

# ```python
# return False
# ```

# Yahin program khatam.

# ---

# # Ye line samjho

# ```python
# if c in closeToOpen:
# ```

# Matlab:

# **Kya current character closing bracket hai?**

# Example:

# ```python
# c = ")"
# ```

# ```python
# ")" in closeToOpen
# ```

# Output:

# ```python
# True
# ```

# Example:

# ```python
# c = "("
# ```

# ```python
# "(" in closeToOpen
# ```

# Output:

# ```python
# False
# ```

# ---

# # Ye line

# ```python
# stack[-1] == closeToOpen[c]
# ```

# Example:

# ```python
# c = "]"
# ```

# Dictionary

# ```python
# closeToOpen[']']
# ```

# Output:

# ```text
# [
# ```

# Agar stack ka top bhi

# ```text
# [
# ```

# hai

# to pop.

# ---

# # Comparison

# | Brute Force                   | Stack                          |
# | ----------------------------- | ------------------------------ |
# | `replace()` use karta hai     | Stack use karta hai            |
# | O(n²)                         | O(n)                           |
# | Interview me kam use hota hai | Interview ka expected solution |
# | Aasaan hai                    | Thoda practice chahiye         |

# **Interview aur LeetCode ke liye Stack wala solution hi best hai**, kyunki uski **Time Complexity = O(n)** hai.
