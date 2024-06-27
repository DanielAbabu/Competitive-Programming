class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c= Counter()
        for ed in edges:
            c.update(ed)
        
        return max(c, key=lambda x: c[x])

        