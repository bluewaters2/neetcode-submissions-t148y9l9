# we can find the mid, reverse the second half of the list
# and then connect the node from 2 lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        
        # find the mid
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        # reverse the second half
        prev, temp = None, None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # combine the 2 lists
        while prev and curr:
            first = curr.next
            second = prev.next
            curr.next = prev
            prev.next = first
            curr = first
            prev = second
        
