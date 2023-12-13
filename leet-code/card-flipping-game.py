class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        minm = float('inf')

        bad=set(i for i,j in zip(fronts,backs) if i==j)
        
        fronts.extend(backs)

        for i in fronts:
            if i not in bad:
                minm=min(minm,i)

        return minm if minm != float('inf') else 0

        # good = {}
        # good = {i: True for i in fronts}
        # mingood = float('inf')
        # g = float('inf')
        # for i in backs: #zoro flip
        #     if i not in set(fronts):
        #         g = i
        #     mingood = min(mingood , g)
        # for i,j in zip(fronts,backs):
        #     if i == j:
        #         good[i] = False
        # for i in fronts:
        #     if good[i]:
        #         mingood = min(i , mingood)
        # return mingood if mingood != float('inf') else 0


