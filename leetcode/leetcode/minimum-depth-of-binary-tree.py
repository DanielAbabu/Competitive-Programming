# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.minm = float('inf')

        def traverse(root, n):

            if not root:
                return 

            if not root.left and not root.right:
                self.minm = min(self.minm, n)
                return    

            traverse(root.left, n+1)
            traverse(root.right, n+1)
        
        traverse(root, 1)
        return 0 if self.minm == float('inf') else self.minm