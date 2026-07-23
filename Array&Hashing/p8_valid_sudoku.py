from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row dupliaction
        for j in range(9):
            row = set()
            for k in range(9):
                if board[j][k] == ".":
                    continue

                if board[j][k] in row:
                    return False

                row.add(board[j][k])

            # column duplication
        for m in range(9):
            col = set()
            for n in range(9):
                if board[n][m] == ".":
                    continue

                if board[n][m] in col:
                    return False

                col.add(board[n][m])

        #         # Check all 3×3 boxes:
        # boxRow = 0

        # boxCol = 0

        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):

                seen = set()

                for i in range(3):

                    for j in range(3):

                        value = board[boxRow + i][boxCol + j]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True


s = Solution()
print(
    s.isValidSudoku(
        board=[
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)


# Ye pura logic **3×3 boxes** check karne ke liye hai. Chalo ek-ek line ko trace karte hain.

# Board:

# ```text
#       0 1 2 | 3 4 5 | 6 7 8
#     -------------------------
# 0 |   1 2 . | . 3 . | . . .
# 1 |   4 . . | 5 . . | . . .
# 2 |   . 9 8 | . . . | . . 3
#     -------------------------
# 3 |   5 . . | . 6 . | . . 4
# 4 |   . . . | 8 . 3 | . . 5
# 5 |   7 . . | . 2 . | . . 6
#     -------------------------
# 6 |   . . . | . . . | 2 . .
# 7 |   . . . | 4 1 9 | . . 8
# 8 |   . . . | . 8 . | . 7 9
# ```

# Sudoku me total **9 boxes** hote hain.

# ```
# ┌───────┬───────┬───────┐
# │ Box 1 │ Box 2 │ Box 3 │
# ├───────┼───────┼───────┤
# │ Box 4 │ Box 5 │ Box 6 │
# ├───────┼───────┼───────┤
# │ Box 7 │ Box 8 │ Box 9 │
# └───────┴───────┴───────┘
# ```

# ---

# # Step 1

# ```python
# for boxRow in range(0, 9, 3):
# ```

# Yeh generate karega:

# ```text
# boxRow

# 0
# 3
# 6
# ```

# Kyun?

# ```python
# range(0,9,3)
# ```

# Matlab

# ```text
# 0 → 3 → 6
# ```

# Ye har 3×3 box ki **starting row** hai.

# ---

# # Step 2

# ```python
# for boxCol in range(0, 9, 3):
# ```

# Ye bhi generate karega:

# ```text
# boxCol

# 0
# 3
# 6
# ```

# Ye har box ki **starting column** hai.

# ---

# Ab dono ko combine karo.

# | boxRow | boxCol | Kaunsa Box    |
# | ------ | ------ | ------------- |
# | 0      | 0      | Top Left      |
# | 0      | 3      | Top Middle    |
# | 0      | 6      | Top Right     |
# | 3      | 0      | Middle Left   |
# | 3      | 3      | Center        |
# | 3      | 6      | Middle Right  |
# | 6      | 0      | Bottom Left   |
# | 6      | 3      | Bottom Middle |
# | 6      | 6      | Bottom Right  |

# Yani outer loops sirf **9 boxes** choose karte hain.

# ---

# # Pehla box

# ```text
# boxRow = 0
# boxCol = 0
# ```

# ```
# 1 2 .
# 4 . .
# . 9 8
# ```

# ---

# # Step 3

# ```python
# seen = set()
# ```

# Har box ke liye naya HashSet.

# ```text
# seen = {}
# ```

# ---

# # Step 4

# ```python
# for i in range(3):
# ```

# Output

# ```text
# 0
# 1
# 2
# ```

# ---

# # Step 5

# ```python
# for j in range(3):
# ```

# Output

# ```text
# 0
# 1
# 2
# ```

# Ab `(i,j)` ki values hongi:

# ```
# (0,0)
# (0,1)
# (0,2)

# (1,0)
# (1,1)
# (1,2)

# (2,0)
# (2,1)
# (2,2)
# ```

# Yeh exactly ek **3×3 grid** ke positions hain.

# ---

# # Sabse important line

# ```python
# value = board[boxRow + i][boxCol + j]
# ```

# Isko trace karte hain.

# ### Pehla iteration

# ```
# boxRow = 0
# boxCol = 0

# i = 0
# j = 0
# ```

# To

# ```python
# board[0+0][0+0]
# ```

# ↓

# ```python
# board[0][0]
# ```

# ↓

# ```
# 1
# ```

# ---

# ### Doosra iteration

# ```
# i = 0
# j = 1
# ```

# ```python
# board[0][1]
# ```

# ↓

# ```
# 2
# ```

# ---

# ### Teesra iteration

# ```
# i = 0
# j = 2
# ```

# ```python
# board[0][2]
# ```

# ↓

# ```
# .
# ```

# ---

# ### Chautha iteration

# ```
# i = 1
# j = 0
# ```

# ```python
# board[1][0]
# ```

# ↓

# ```
# 4
# ```

# ---

# ### Paanchwa

# ```
# i = 1
# j = 1
# ```

# ↓

# ```python
# board[1][1]
# ```

# ↓

# ```
# .
# ```

# ---

# Isi tarah poora box:

# ```
# board[0][0]
# board[0][1]
# board[0][2]

# board[1][0]
# board[1][1]
# board[1][2]

# board[2][0]
# board[2][1]
# board[2][2]
# ```

# check ho gaya.

# ---

# # Ab second box

# Outer loop badlega

# ```
# boxRow = 0
# boxCol = 3
# ```

# Ab line banegi

# ```python
# board[boxRow+i][boxCol+j]
# ```

# Matlab

# ```
# board[0][3]
# board[0][4]
# board[0][5]

# board[1][3]
# board[1][4]
# board[1][5]

# board[2][3]
# board[2][4]
# board[2][5]
# ```

# Ye second 3×3 box hai.

# ---

# # Third Box

# ```
# boxRow=0
# boxCol=6
# ```

# Banega

# ```
# board[0][6]
# board[0][7]
# board[0][8]

# board[1][6]
# board[1][7]
# board[1][8]

# board[2][6]
# board[2][7]
# board[2][8]
# ```

# ---

# Isi tarah total 9 boxes check ho jate hain.

# # Visual

# ```
# Outer Loop

# boxRow = 0
# boxCol = 0

#         ↓

# 1 2 .
# 4 . .
# . 9 8

# -------------------

# boxRow = 0
# boxCol = 3

#         ↓

# . 3 .
# 5 . .
# . . .

# -------------------

# boxRow = 0
# boxCol = 6

#         ↓

# . . .
# . . .
# . . 3

# -------------------

# ...

# Total 9 boxes
# ```

# ---

# ## Ye line yaad rakhna

# ```python
# # board[boxRow + i][boxCol + j]
# # ```

# # Isme:

# # * `boxRow` = kis 3×3 box ki starting row.
# # * `boxCol` = kis 3×3 box ka starting column.
# # * `i` = us box ke andar row offset (`0,1,2`).
# # * `j` = us box ke andar column offset (`0,1,2`).

# # Formula:

# # ```text
# # Final Row    = boxRow + i
# # Final Column = boxCol + j
# # ```

# # Yehi poore 3×3 box ko access karne ki trick hai, aur Sudoku interviews me ye bahut common pattern hai.


# Ye sabse important line hai. Isko bahut simple tareeke se samajhte hain.

# Board ko number de dete hain:

# ```text
#       0 1 2 | 3 4 5 | 6 7 8
#     -------------------------
# 0 |   1 2 . | . 3 . | . . .
# 1 |   4 . . | 5 . . | . . .
# 2 |   . 9 8 | . . . | . . 3
#     -------------------------
# 3 |   5 . . | . 6 . | . . 4
# 4 |   . . . | 8 . 3 | . . 5
# 5 |   7 . . | . 2 . | . . 6
#     -------------------------
# 6 |   . . . | . . . | 2 . .
# 7 |   . . . | 4 1 9 | . . 8
# 8 |   . . . | . 8 . | . 7 9
# ```

# ---

# # Pehle sirf ye samjho

# ```python
# boxRow = 0
# boxCol = 0
# ```

# Matlab hum **first (top-left) 3×3 box** me hain.

# Ab loop chalta hai

# ```python
# for i in range(3):
#     for j in range(3):
# ```

# To values hongi:

# ```
# i = 0,1,2
# j = 0,1,2
# ```

# ---

# ## 1st Iteration

# ```
# i = 0
# j = 0
# ```

# Line:

# ```python
# board[boxRow + i][boxCol + j]
# ```

# Numbers daalo:

# ```python
# board[0 + 0][0 + 0]
# ```

# ↓

# ```python
# board[0][0]
# ```

# ↓

# ```
# 1
# ```

# ---

# ## 2nd Iteration

# ```
# i = 0
# j = 1
# ```

# ```python
# board[0+0][0+1]
# ```

# ↓

# ```python
# board[0][1]
# ```

# ↓

# ```
# 2
# ```

# ---

# ## 3rd Iteration

# ```
# i = 0
# j = 2
# ```

# ```python
# board[0][2]
# ```

# ↓

# ```
# .
# ```

# ---

# ## 4th Iteration

# ```
# i = 1
# j = 0
# ```

# ```python
# board[0+1][0+0]
# ```

# ↓

# ```python
# board[1][0]
# ```

# ↓

# ```
# 4
# ```

# ---

# ## 5th Iteration

# ```
# i = 1
# j = 1
# ```

# ↓

# ```python
# board[1][1]
# ```

# ↓

# ```
# .
# ```

# ---

# Aise hi aage chalega.

# Poora first box check ho jayega.

# ```
# board[0][0]
# board[0][1]
# board[0][2]

# board[1][0]
# board[1][1]
# board[1][2]

# board[2][0]
# board[2][1]
# board[2][2]
# ```

# ---

# # Ab sawal:

# ## `+` kyun kiya?

# Suppose tum second box me chale gaye.

# Ab

# ```python
# boxRow = 0
# boxCol = 3
# ```

# Matlab ye box:

# ```
# . 3 .
# 5 . .
# . . .
# ```

# Agar tum likhte

# ```python
# board[i][j]
# ```

# to kya milta?

# ```
# board[0][0]
# board[0][1]
# board[0][2]
# ...
# ```

# Fir se first box hi milta. ❌

# ---

# Lekin jab tum likhte ho

# ```python
# board[boxRow + i][boxCol + j]
# ```

# To

# ### First iteration

# ```
# i = 0
# j = 0
# ```

# ban gaya

# ```python
# board[0+0][3+0]
# ```

# ↓

# ```python
# board[0][3]
# ```

# ---

# Second

# ```
# i = 0
# j = 1
# ```

# ↓

# ```python
# board[0][4]
# ```

# ---

# Third

# ↓

# ```python
# board[0][5]
# ```

# ---

# Fourth

# ↓

# ```python
# board[1][3]
# ```

# Ab dekho.

# Hum automatically second box me aa gaye.

# ```
# board[0][3]
# board[0][4]
# board[0][5]

# board[1][3]
# board[1][4]
# board[1][5]

# board[2][3]
# board[2][4]
# board[2][5]
# ```

# ---

# # Isliye `+` use kiya.

# `i` aur `j` sirf **box ke andar movement** karte hain:

# ```
# 0 1 2
# 0 1 2
# 0 1 2
# ```

# Aur

# ```
# boxRow
# boxCol
# ```

# batate hain ki **kis box se start karna hai**.

# Formula yaad rakho:

# ```
# Final Row    = boxRow + i
# Final Column = boxCol + j
# ```

# * `boxRow` = box ki starting row (0, 3, ya 6)
# * `i` = us box ke andar row (0, 1, 2)
# * `boxCol` = box ki starting column (0, 3, ya 6)
# * `j` = us box ke andar column (0, 1, 2)

# ---

# ### Ab main tumse ek question poochta hoon.

# Agar:

# ```python
# boxRow = 3
# boxCol = 6

# i = 2
# j = 1
# ```

# To ye line:

# ```python
# board[boxRow + i][boxCol + j]
# ```

# kis index par jayegi?

# Khud calculate karke batao:

# ```
# board[ ? ][ ? ]
# ```

# Agar ye answer tum nikaal loge, to ye `+` wala concept hamesha ke liye clear ho jayega.
