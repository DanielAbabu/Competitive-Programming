class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list(word1)
        list(word2)
        ans=[]
        for i in range(min(len(word1),len(word2))):
            ans.append(word1[i])
            ans.append(word2[i])
        i+=1
        ans.extend(word1[i:])
        ans.extend(word2[i:])
        return "".join(ans)