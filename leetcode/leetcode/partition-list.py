# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dl = left = ListNode(0)
        dr = right = ListNode(0)
        
        curr = head

        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next

            curr = curr.next
        left.next = dr.next
        right.next = None
        return dl.next
        

