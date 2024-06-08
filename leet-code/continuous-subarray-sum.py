class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0: -1}  
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            rem = summ % k

            if rem in hmap:
                if i - hmap[rem] > 1:
                    return True
            else:
                hmap[rem] = i

        return False