class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        c=0
        m=0
        for i in range(len(flips)):
            m=max(m,flips[i])
            if i+1 == m:
                c+=1
        return c

        