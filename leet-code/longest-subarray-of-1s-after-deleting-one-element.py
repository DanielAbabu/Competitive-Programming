class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = summ = maxm = 0

        for j in range(len(nums)):
            summ += nums[j]
            if j-i > summ:
                summ -= nums[i]
                i+=1
        
            maxm = max(maxm, j-i)
        
        return maxm

