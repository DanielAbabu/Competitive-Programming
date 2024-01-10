class Solution:
    def findAnagrams(self, s: str, p: str):
        n = len(p)
        tem = Counter(s[:n])
        p = Counter(p)

        ans=[]
        if tem == p:
            ans.append(0)

        for i in range(n,len(s)):
            tem[s[i]] += 1
            tem[s[i-n]] -= 1

            if tem[s[i-n]] == 0:
                del tem[s[i-n]]

            if tem == p:
                ans.append(i-n+1)
        return ans
            
