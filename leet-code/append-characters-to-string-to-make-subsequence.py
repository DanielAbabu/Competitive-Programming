class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for a in s:
            if i == len(t):
                return 0

            if t[i] == a:
                i +=1 

        return len(t) - i

