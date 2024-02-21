# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        while n:
            if not fast.next: 
                return head.next 
            fast = fast.next
            n-=1

        while fast.next: 
            fast= fast.next
            slow =slow.next
            
        slow.next = slow.next.next
        return head