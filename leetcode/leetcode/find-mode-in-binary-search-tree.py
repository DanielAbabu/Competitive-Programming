# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        

        d = defaultdict(int)
        def traverse(root):
            if not root:
                return 
            
            traverse(root.left)
            d[root.val] += 1
            traverse(root.right)
        
        traverse(root)
        m = max(d, key = lambda x : d.get(x))
        ans = []
        print(d,m)
        for k,v in d.items():
            if v == d[m]:
                ans.append(k)

        return ans