class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        dit={}

        for i in s:
            dit[int(i[-1])] = i[:-1]
        
        ans=[]
        for i in range(len(s)):
            ans.append(dit[i+1])
        
        return " ".join(ans)