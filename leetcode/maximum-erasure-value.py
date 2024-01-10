class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        times = defaultdict(int)
        j=0
        summ = maxm = 0
        

        for i in range(len(nums)):
            times[nums[i]] += 1
            summ += nums[i]


            while times[nums[i]] > 1:
                times[nums[j]] -= 1
                summ -= nums[j]
                j+=1

            maxm = max(maxm,summ)
        
        return maxm
        