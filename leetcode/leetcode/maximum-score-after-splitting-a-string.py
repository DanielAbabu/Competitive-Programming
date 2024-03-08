class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(list(map(int,list(s))))
        zero = maxm = 0


        for i in range(len(s)-1):
            if s[i] == "0":
                zero += 1
            else:
                ones -= 1

            maxm = max(maxm, zero + ones)
        
        return maxm
