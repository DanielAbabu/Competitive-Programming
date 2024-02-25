class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        res = [-1] * len(nums)

        for i, num in enumerate(nums):              
            while stk and nums[stk[-1]] < num:
                res[stk.pop()] = num

            stk.append(i)

        for i, num in enumerate(nums):              
            while stk and nums[stk[-1]] < num:
                res[stk.pop()] = num
                
        return res