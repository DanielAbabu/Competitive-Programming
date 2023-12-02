class Solution:
    def freqAlphabets(self, s: str) -> str:
        s=list(s)[::-1]
        ans=[]
        i=0
        while i < len(s):
            if s[i] == "#":
                ans.append(chr(96+int(s[i+1])+ int(s[i+2])*10))
                i+=2
            else:
                ans.append(chr(96+int(s[i])))
            i+=1
        ans=ans[::-1]
        return "".join(ans)
                
