class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        tot , res = 0 , 0

        for right in range(len(nums)):
            tot += nums[right]

            if nums[right]*(right - left+1) > tot+k:
                tot -= nums[left]
                left += 1

            res=max(res, right - left+1 )

        return res