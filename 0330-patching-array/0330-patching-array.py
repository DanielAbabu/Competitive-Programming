class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        if n != nums[-1]:
            nums.append(n)

        maxm = count = i = 0
        while maxm < n:
            if i<len(nums) and (maxm < nums[i]-1):
                maxm += (maxm + 1)
                count += 1
            else:
                maxm += nums[i]
                i+=1

        return count
