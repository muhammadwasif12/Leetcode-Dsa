from typing import Optional
from typing import Node

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        oldToCopy = {None: None}

        # 1. Har original node ki copy banao
        cur = head

        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        # 2. next aur random pointers connect karo
        cur = head

        while cur:
            copy = oldToCopy[cur]

            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]

            cur = cur.next

        # 3. Copied list ka head return karo
        return oldToCopy[head]
