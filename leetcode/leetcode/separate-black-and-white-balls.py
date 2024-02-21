class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        tem = len(s)-1
        for i in range(len(s)-1,-1,-1):
            if(s[i] == "1"):
                ans += tem - i
                tem -= 1
        return ans