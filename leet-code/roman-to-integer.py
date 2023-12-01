class Solution:
    def romanToInt(self, s: str) -> int:
        rom={ "I":1 , "V":5, "X":10, "L":50, "I":1, "C":100, "D":500, "M":1000}
        x=0
        for i in range(len(s)):
            if i+1 < len(s) and rom[ s[i] ] < rom[ s[i+1] ]:
                x-= rom[ s[i] ]
            else:
                x+= rom[ s[i] ]
        return x