class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        curr = sum(cardPoints[:n])
        minm = curr

        for i in range(n,len(cardPoints)):
            curr += cardPoints[i]
            curr -= cardPoints[i-n]

            minm = min(minm, curr)
        
        return sum(cardPoints) - minm
