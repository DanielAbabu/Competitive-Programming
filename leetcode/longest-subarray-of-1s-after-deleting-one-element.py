class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = summ = j = 0

        for i, num in enumerate(nums):
            summ += num
            if summ < i - j:
                summ -= nums[j]
                j += 1
            
            ans = max(ans, i - j)

        return ans
