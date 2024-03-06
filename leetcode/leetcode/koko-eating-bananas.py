class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def fast(sp):
            tot = 0
            for pile in piles:
                tot += ceil(pile/sp)
            
            return tot
        
        while l < r:
            m = (l+r)//2

            if fast(m) <= h:
                r = m
            else:
                l = m +1 
        
        return l
