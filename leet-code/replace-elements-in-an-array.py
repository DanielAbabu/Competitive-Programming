class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        count = {} 
        for i,num in enumerate(nums):
            count[num] = i 
        
        for key,value in operations:
            locate = count[key] 
            nums[locate] = value 
            del count[key]   
            count[value] = locate
            
        return nums
