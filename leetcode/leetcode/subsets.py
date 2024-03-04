class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        buck = []
        ans = []
        def backtrack(i):
            ans.append(buck.copy())
            if i == len(nums):
                return
            for j in range(i,len(nums)):
                buck.append(nums[j])
                backtrack(j+1)
                buck.pop()
            
        backtrack(0)
        return ans
            