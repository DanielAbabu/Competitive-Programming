class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = ans = 0 
        for i in s:
            if i == "(":
                c += 1
            else:
                if c == 0:
                    ans += 1
                else:
                    c -= 1
        return ans + c
