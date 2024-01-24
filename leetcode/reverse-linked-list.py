# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newl = None
        curr = head

        while curr:
            dummy = curr.next
            curr.next = newl
            newl = curr
            curr = dummy
        
        return newl