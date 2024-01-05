class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        n=len(nums)
        for i in range(n):
            left=i+1
            right=n-1
            target=-nums[i]
            while left<right:
                if target==nums[left]+nums[right]:
                    ans.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif target<nums[left]+nums[right]:
                    right-=1
                else:
                    left+=1
        return ans
            
        
                    
                
                    