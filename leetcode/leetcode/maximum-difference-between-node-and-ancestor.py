# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        val = []
        arr = []
        def search(node):
            if not node:
                return 

            arr.append(node.val)
            if not node.left and not node.right:
                tem = sorted(arr)
                val.append( tem[-1] - tem[0])

            if node.right:
                search(node.right)
                arr.pop()

            if node.left:
                search(node.left)
                arr.pop()


        search(root)


        return max(val)

            