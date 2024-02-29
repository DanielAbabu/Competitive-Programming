# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, lef=None):
#         self.val = val
#         self.left = left
#         self.lef = lef
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, minm, maxm):
            if not node:
                return True

            
            if node.val <= minm or node.val >= maxm:
                print(node.val, minm, maxm)
                return False
            
            return valid(node.left, minm, node.val) and valid(node.right, node.val, maxm)
                

        return valid(root,float('-inf'), float('inf'))
