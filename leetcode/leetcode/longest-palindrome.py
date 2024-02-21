class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = Counter(s)
        ans = 0
        t=False
        
        for i,c in h.items():
            if c % 2 != 0:
                ans += c-1
                t = True
            else:
                ans += c

        return ans + 1 if t else ans

