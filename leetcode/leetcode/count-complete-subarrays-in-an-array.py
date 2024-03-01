class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c = i = j = 0
        k = len(set(nums))

        for i in range(len(nums)):
            s = set()
            for j in range(i,len(nums)):
                s.add(nums[j]) 
                if len(s) == k:
                    c += 1
 

        return c


        