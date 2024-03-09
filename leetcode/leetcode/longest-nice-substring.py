class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        check = set(s)

        for i in range(len(s)):

            if s[i].lower() in check  and  s[i].upper() in check:
                continue

            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i+1:])

            return max(left, right, key=len)

        return s      