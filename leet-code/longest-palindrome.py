class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        ans = 0
        c = 0
        for b in a:
            if a[b] % 2 == 0:
                ans += a[b]
            else:
                c = 1
                ans += (a[b]-1)
        
        return ans + c