from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Koko ki minimum possible speed 1 banana/hour hai
        left = 1

        # Maximum possible speed = sabse badi pile
        # Agar k = largest pile hai, to har pile maximum 1 hour mein finish ho sakti hai
        right = max(piles)

        # Jab tak search range valid hai
        while left <= right:

            # Beech wali eating speed try karo
            # Example: left=1, right=4 → k=2
            k = (left + right) // 2

            # Is speed par total kitne hours lagenge
            hours = 0

            # Har banana pile ko check karo
            for pile in piles:

                # Is pile ko finish karne mein kitne hours lagenge
                # ceil(pile / k)
                #
                # Example:
                # pile = 7, k = 3
                # (7 + 3 - 1) // 3
                # = 9 // 3
                # = 3 hours
                hours += (pile + k - 1) // k

            # Agar Koko given h hours ke andar finish kar sakti hai
            if hours <= h:

                # Ye k valid hai
                # Lekin hume minimum k chahiye
                # Isliye aur chhoti speed search karo
                right = k - 1

            else:

                # Koko bohot slow hai
                # Required hours h se zyada hain
                # Isliye bigger speed search karo
                left = k + 1

        # Jab binary search finish hogi,
        # left sabse chhoti valid eating speed hogi
        return left


s = Solution()

# piles = [1,4,3,2], h = 9
# Answer = 2
print(s.minEatingSpeed([1, 4, 3, 2], 9))

# piles = [25,10,23,4], h = 4
# Answer = 25
print(s.minEatingSpeed([25, 10, 23, 4], 4))
