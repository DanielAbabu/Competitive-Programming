class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        tot = 0
        for i in range(len(nums)):
            find = bisect_right(nums,target - nums[i])

            length = find - i
            if length > 0:
                tot += pow(2, length - 1, (10**9 +7))

        return tot % (10**9 +7)

