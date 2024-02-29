# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        ans = []
        def traverse(root):
            if not root:
                return
            
            arr.append(str(root.val))
            if not root.right and  not root.left:

                ans.append( int("".join(arr)) )
            

            if root.right:
                traverse(root.right)
                arr.pop()
            
            if root.left:
                traverse(root.left)
                arr.pop()
        
        traverse(root)
        return sum(ans)
