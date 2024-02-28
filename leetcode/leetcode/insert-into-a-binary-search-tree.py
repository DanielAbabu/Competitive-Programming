# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        

        def ins(curr,val):
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return True

                self.insertIntoBST(curr.left,val)

            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return True

                self.insertIntoBST(curr.right,val)

        ins(root,val)
        return root
