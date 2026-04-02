# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        first, second = dummy, dummy
        first.next, second.next = head, head

        for _ in range(n):
            first = first.next

        while first and first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next