class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = maxm = 0
        answer = {"T":0, "F":0}   

        for j in range(len(answerKey)): 
            answer[answerKey[j]] += 1    

            if min(answer["F"], answer["T"]) > k:     
                answer[answerKey[i]] -= 1            
                i += 1      

            maxm = max(maxm,j-i+1) 

        return maxm 