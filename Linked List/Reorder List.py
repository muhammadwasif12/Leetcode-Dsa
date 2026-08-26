from typing import ListNode

# Slow and fast pointer


class Solution:
    def reorderList(self, head: ListNode) -> None:

        slow = head
        fast = head.next

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split
        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
