class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        times = defaultdict(int)
        maxm=0
        j=0

        for i in range(len(s)):
            times[s[i]] += 1 
             
            while times[s[i]] > 1:
                times[s[j]] -= 1
                j+=1

            maxm = max(maxm,i-j+1)
        
        return maxm


#     a b b a 
# i   ^
# j        ^
# 
#  a:0  b:2  c:2
# 
# 
# c 2
# m 2
# 