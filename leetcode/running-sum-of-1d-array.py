class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum=[]
        cur=0
        for i in nums:
            cur+=i
            runsum.append(cur)
        return runsum
