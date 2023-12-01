class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count=dict(map(reversed,enumerate(order)))

        ans=sorted(words, key = lambda word: [count[ch] for ch in word])
        return ans == words

        
        