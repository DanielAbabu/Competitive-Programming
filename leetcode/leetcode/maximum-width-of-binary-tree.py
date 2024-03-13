# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = {}
        self.maxm = 0

        def traversal(root, i, lvl):
            if root is None:
                return 

            dic.setdefault(lvl, [i, i])

            dic[lvl][0] = min(dic[lvl][0], i)
            dic[lvl][1] = max(dic[lvl][1], i)

            self.maxm = max(self.maxm, dic[lvl][1] - dic[lvl][0])

            traversal(root.left, 2*i, lvl+1)
            traversal(root.right, 2*i+1, lvl+1)

        traversal(root, 0, 0)

        return self.maxm + 1