class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=[0]*(max(nums)+1)
        ans=[]
        for num in nums:
            s[num]+=1
        for num in nums:
            ans.append(sum(s[:num])) 
        return ans

        