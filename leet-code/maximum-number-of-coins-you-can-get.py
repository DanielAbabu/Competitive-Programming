class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        me=0
        piles.sort()
        time=len(piles)//3
        for i in range(time):             
            me+=piles[-(2+(2*i))]
        return me
