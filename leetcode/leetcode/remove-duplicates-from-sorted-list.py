# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
            
        slow = head
        fast = head.next
        
        while fast != None:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next

        return head


            