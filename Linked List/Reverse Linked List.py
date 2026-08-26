class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# Linked List banao:
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)


# Reverse
s = Solution()
result = s.reverseList(head)


# Print Linked List
while result:
    print(result.val, end=" → ")
    result = result.next

print("None")
