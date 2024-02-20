class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i in range(len(nums)):
            far = max(far , i+nums[i])
            if far >= len(nums)-1 :
                return True
            if far <= i:
                break
        return False