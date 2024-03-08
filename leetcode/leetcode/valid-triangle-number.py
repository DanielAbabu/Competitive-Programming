class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums)-2): 
            j = i+1
            for k in range(i+2,len(nums)):
               
                while j < k and nums[i] + nums[j] <= nums[k]:
                    j += 1

                ans += k - j
        
        return ans