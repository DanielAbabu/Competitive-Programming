class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        p1 = p2 = 0
        c = 0

        while p1<len(g) and p2<len(s):
            if g[p1] > s[p2]:
                p2+=1
            else:
                c+=1
                p1+=1
                p2+=1
        return c