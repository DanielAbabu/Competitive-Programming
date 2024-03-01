class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm = float('-inf')
        val = 0

        for i in range(len(nums)):
            val += nums[i]

            maxm = max(maxm,val)
            if val < 0:
                val =0

        return maxm