from typing import ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # fast ko n steps aage le jao
        for _ in range(n):
            fast = fast.next

        # dono ko move karo
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow ke next node ko remove karo
        slow.next = slow.next.next

        return dummy.next
