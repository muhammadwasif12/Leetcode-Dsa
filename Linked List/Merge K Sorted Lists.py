# brute force

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode
from typing import List
from typing import Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next





    #iteration

    class Solution:
     def mergeKLists(self, lists):

        # Agar koi list hi nahi hai
        if not lists:
            return None

        # Har next list ko previous merged result ke saath merge karo
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i - 1], lists[i])

        # Last position par complete merged list hai
        return lists[-1]


    def mergeTwoLists(self, list1, list2):

        # Dummy node
        dummy = ListNode(0)

        # Result list banane ke liye pointer
        cur = dummy

        # Jab tak dono lists mein nodes hain
        while list1 and list2:

            # Chhoti value wala node result mein lagao
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            # Result pointer ko aage move karo
            cur = cur.next

        # Jo list baqi bach gayi hai usko attach karo
        cur.next = list1 or list2

        # Actual head return karo
        return dummy.next
