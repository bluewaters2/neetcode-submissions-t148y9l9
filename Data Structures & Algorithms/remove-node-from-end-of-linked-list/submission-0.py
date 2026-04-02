# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        dummy = ListNode()
        p = dummy
        p.next = head
        
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        for _ in range(l - n):
            p = p.next
        
        p.next = p.next.next

        return dummy.next