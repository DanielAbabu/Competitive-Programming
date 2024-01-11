class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        win = Counter(s[:k])
        vowel = {'a', 'e', 'i', 'o', 'u'}
        count = maxm = 0

        for i in win:
            if i in vowel:
                count += win[i]

        maxm= max(maxm, count)

        for i in range(k,len(s)):
            if s[i] in vowel:
                count +=1
            
            if s[i-k] in vowel:
                count -=1
            
            maxm = max(maxm, count)

        return maxm


