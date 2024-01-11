class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        win = Counter(s2[:n])
        s1 = Counter(s1)

        if win == s1:
            return True
        for i in range(n,len(s2)):
            win[s2[i]] += 1
            win[s2[i-n]] -= 1

            if win[s2[i-n]] == 0:
                del win[s2[i-n]]

            if win == s1:
                return True
        
        return False
