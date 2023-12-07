class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nu=[]
        for i in range(n):
            nu.append(nums[i])
            nu.append(nums[i+n])
        return nu