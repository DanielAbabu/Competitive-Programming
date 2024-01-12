class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ind = {}
        minm = float('inf')

        for i,ch in enumerate(cards):
            if ind.get(ch,-1) != -1:
                minm = min(minm, i-ind[ch]+1)
            ind[ch] = i
        
        return -1 if minm == float('inf') else minm
        