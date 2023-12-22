class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        minm = float('inf')
        aver = float('inf')

        for i in range(len(nums)):
            
            minm = min(minm, nums[i])

            if nums[i] > aver :
                return True

            if nums[i] > minm:
                aver = nums[i]

        return False