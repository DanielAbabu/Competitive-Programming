class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shi=[0]*(len(s)+2)

        for i in range(len(shifts)):
            if shifts[i][2] == 0:
               shi[shifts[i][0]+1] += -1
               shi[shifts[i][1]+2] += 1
            else:
                shi[shifts[i][0]+1] += 1
                shi[shifts[i][1]+2] += -1
        for i in range(1,len(shi)):
            shi[i] += shi[i-1]
        
        
        s=list(s)

        for i in range(len(s)):
            s[i] = chr((ord(s[i]) + shi[i+1] - 97)%26 + 97)
        
        return "".join(s)
