class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxm=0
        nums.sort()
        for i in range(len(nums)-2):
            win=nums[i:i+3]

            if win[0]+win[1] > win[2] and win[2]+win[0] > win[1] and win[1]+win[2] > win[0]:
                maxm=max(maxm,sum(win))
              
        return maxm