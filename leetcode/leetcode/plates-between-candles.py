class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        prefix = []
        candle = []
        ctem = -1
        ptem = 0
        for i in range(len(s)):
            if s[i] == "|":
                ctem = i            
                candle.append(ctem)
            else:
                ptem += 1

            prefix.append(ptem)
        
        if not candle:
            candle = [0]
            

        ans = []
        print(prefix)
        print(candle)
        for q in queries:
            l = bisect_left(candle, q[0]) 
            r = bisect_right(candle, q[1])
            
            if r == 0:
                r = 1
            if l == len(candle):
                l -= 1

            r -= 1
            
            print(r,l)
            ans.append( max(prefix[candle[r]] - prefix[candle[l]], 0) )

        return ans
        
