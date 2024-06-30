class Unionfind: 
    def __init__(self, n): 
        self.count = n
        self.rank = [1] * n 
        self.parent = [i for i in range(n)] 
  
    def find(self, x): 
        if (self.parent[x] != x): 
            self.parent[x] = self.find(self.parent[x])   

        return self.parent[x] 
  
    def union(self, x, y): 
        xset = self.find(x) 
        yset = self.find(y) 
  
        if xset == yset: 
            return False
            
        self.count -= 1
        if self.rank[xset] < self.rank[yset]: 
            self.parent[xset] = yset 
  
        elif self.rank[xset] > self.rank[yset]: 
            self.parent[yset] = xset 

        else: 
            self.parent[yset] = xset 
            self.rank[xset] = self.rank[xset] + 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = Unionfind(n)
        bob = Unionfind(n)
        ans = 0

        edges.sort(reverse=True)
        for t, a, b in edges:
            a -= 1
            b -= 1
            if t == 3 and not (alice.union(a,b) and bob.union(a,b)):
                ans += 1
            elif t == 2  and not bob.union(a,b):
                ans += 1
            elif t == 1  and not alice.union(a,b):
                ans += 1

        return ans if alice.count == 1 and bob.count == 1 else -1