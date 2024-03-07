class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        buck = []
        ans = []
        def backtrack():

            if  len(buck) >= len(nums):
                if len(buck) == len(nums):
                    ans.append(buck[:])
                return
            
            for j in range(len(nums)):
                
                if nums[j] not in buck:
                    buck.append(nums[j])
                    backtrack()
                    buck.pop() 


        backtrack()
        return ans

