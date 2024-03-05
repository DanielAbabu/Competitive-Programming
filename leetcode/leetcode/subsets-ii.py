class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        buck = []
        ans = []
        nums.sort()
        def backtrack(i):
            ans.append(buck[:])
            if i >= len(nums):
                return

            val = None
            for j in range(i,len(nums)):
                if val != nums[j]:
                    buck.append(nums[j])
                    backtrack(j+1)
                    val = buck.pop()
            
        backtrack(0)
        return ans
