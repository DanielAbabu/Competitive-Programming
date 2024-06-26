# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def iot(node):
            if not node:
                return []
            return iot(node.left) + [node.val] + iot(node.right)
        
        arr = iot(root)
        
        def solve(nums):
            if not nums:
                return None
            m = len(nums) // 2
            root = TreeNode(nums[m])
            root.left = solve(nums[:m])
            root.right = solve(nums[m+1:])
            return root
        
        return solve(arr)

        