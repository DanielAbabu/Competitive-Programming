class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, largestCount = 0, 0
        arr = collections.Counter()
        for idx in range(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen