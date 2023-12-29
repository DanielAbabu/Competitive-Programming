class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        di=Counter(nums)
        num=sorted(list(set(nums)))

        ans=0
        for i,ch in enumerate(num):
            ans+= di[ch]*i

        return ans
