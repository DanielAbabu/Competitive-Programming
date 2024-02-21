class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxm = summ = nums[0]
        for i in range(1,len(nums)):
            summ += nums[i]
            maxm = max(maxm,math.ceil(summ/(i+1)))

        return maxm
