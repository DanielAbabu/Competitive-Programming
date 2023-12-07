class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=set(nums)
        n=len(nums)//3
        ans=[]
        for i in s:
            if nums.count(i)>n:
                ans.append(i)
        return ans