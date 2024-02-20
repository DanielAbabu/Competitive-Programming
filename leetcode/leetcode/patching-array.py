class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        if n != nums[-1]:
            nums.append(n)

        maxm = c = j = 0
        while maxm < n:
            if j<len(nums) and (maxm < nums[j]-1):
                maxm += (maxm + 1)
                c += 1
            else:
                maxm += nums[j]
                j+=1

        return c
