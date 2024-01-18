class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        tot = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                tot *= nums[i]
            else:
                zeros.append(i)

        ans = []
        for i in range(len(nums)):
            if nums[i] == 0 and len(zeros) == 1:
                ans.append(tot)
            elif len(zeros) > 0:
                ans.append(0)
            else:
                ans.append(tot//nums[i]) 

        return ans