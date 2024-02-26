class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        last = self.getRow(n-1)
        new = [1]
        for i in range(len(last)-1):
            new.append(last[i] + last[i+1])

        new.append(1)
        
        return new


