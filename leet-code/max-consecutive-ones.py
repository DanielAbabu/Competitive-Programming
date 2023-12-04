class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur,maxm=0,0
        for i in nums:
            if i == 1:
                cur+=1
            else:
                cur=0
            maxm=max(maxm,cur)
        return maxm