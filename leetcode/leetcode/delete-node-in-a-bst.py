# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root


        def minm(curr):
            while curr.left:
                curr = curr.left
            return curr

             

        def find(curr,key):
            if not curr:
                return curr

            if curr.val > key:
                curr.left = find(curr.left,key)

            elif curr.val < key:
                curr.right = find(curr.right,key)  

            else:
                if not curr.left:
                    return curr.right
                    
                elif not curr.right:
                    return curr.left
                    
                
                tem = minm(curr.right)
                curr.val = tem.val

                curr.right = find(curr.right,tem.val)
            return curr
        
        return find(root,key)

        

        