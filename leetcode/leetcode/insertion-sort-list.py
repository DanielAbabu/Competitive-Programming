# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode() 
        curr = head
        while curr:
            check = sort
            while check.next and curr.val >= check.next.val:
                check = check.next
                
            tmp = check.next 
            check.next = curr
            curr = curr.next
            check.next.next = tmp
            
        return sort.next