class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        for i in nums:
            if i!=s:
                return s
            s+=1
        return int(nums[-1]) +1