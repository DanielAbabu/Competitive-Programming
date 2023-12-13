class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nu=set(nums)
        for i in range(len(nums)):
            z=target-nums[i]
            if z in nu and i!=nums.index(z):
                return [i,nums.index(z)]