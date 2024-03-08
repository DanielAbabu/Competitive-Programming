# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        c = 0
        temp = head

        while temp:
            c += 1
            temp = temp.next

        v = c // k
        r = c % k

        ans = []
        curr = head

        for i in range( k ):
            size = v

            if i < r:
                size += 1

            ans.append(curr)

            for j in range( size - 1 ):
                if curr:
                    curr = curr.next

            if curr:
                temp = curr.next
                curr.next = None
                curr = temp

        return ans
