class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minm = float('inf')
        summ = j = 0

        for i in range(len(nums)):
            summ += nums[i]
            while summ >= target:
                minm = min(minm, i-j+1)
                summ -= nums[j]
                j += 1
        
        return 0 if minm == float('inf') else minm
            