from typing import ListNode

class Solution:
    def addTwoNumbers(self, l1, l2):

        # Dummy node banaya, result list iske baad se start hogi
        dummy = ListNode(0)

        # cur batayega ke new node kahan add karna hai
        cur = dummy

        # Starting mein koi carry nahi hai
        carry = 0

        # Jab tak l1, l2 ya carry mein kuch baqi hai
        while l1 or l2 or carry:

            # Agar l1 mein node hai to uski value lo
            # warna 0 lo
            val1 = l1.val if l1 else 0

            # Agar l2 mein node hai to uski value lo
            # warna 0 lo
            val2 = l2.val if l2 else 0

            # Dono digits + previous carry ko add karo
            total = val1 + val2 + carry

            # Current digit nikalo
            # Example: 18 % 10 = 8
            digit = total % 10

            # Next addition ke liye carry nikalo
            # Example: 18 // 10 = 1
            carry = total // 10

            # Result list mein current digit ka new node banao
            cur.next = ListNode(digit)

            # cur ko newly created node par move karo
            cur = cur.next

            # l1 ko next node par move karo
            # Agar l1 khatam ho gayi to None
            l1 = l1.next if l1 else None

            # l2 ko next node par move karo
            # Agar l2 khatam ho gayi to None
            l2 = l2.next if l2 else None

        # Dummy ke andar 0 tha, actual answer dummy.next se start hota hai
        return dummy.next
