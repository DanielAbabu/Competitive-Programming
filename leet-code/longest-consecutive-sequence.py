class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c=1
        maxm=1
        nums.sort()

        for i in range(len(nums)-1):
            if abs(nums[i+1]-nums[i]) ==1:
                c+=1
                maxm = max(maxm,c)
            elif abs(nums[i+1]-nums[i]) == 0:
                continue
            else:
                c=1

        return maxm if nums else 0