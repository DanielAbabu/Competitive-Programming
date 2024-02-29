# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dep = defaultdict(list)
        dep[0].append( root.val )
        
        def collect(root,depth):
            if not root:
                return []

            if root.right:
                dep[depth].append( collect(root.right, depth + 1 ))

            if root.left:
                dep[depth].append( collect(root.left, depth + 1 ))

            return root.val

        collect(root, 1)

        answer = []
        for i in range(len(dep)):
            if i % 2 == 0:
                dep[i].reverse()
            answer.append(dep[i])

        return answer
