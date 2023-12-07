class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={ indices[i]:s[i] for i in range(len(s))}
        dic=dict(sorted(dic.items()))
        ans=[]
        for i in range(len(dic)):
          ans.append(dic[i])
        return "".join(ans)
        