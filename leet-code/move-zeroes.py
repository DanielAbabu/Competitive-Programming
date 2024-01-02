class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zp = 0
        for ip in range(len(nums)):
            if nums[ip] != 0:
                nums[ip] , nums[zp] = nums[zp] , nums[ip]
                zp += 1