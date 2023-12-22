class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        tot=sum(nums)
        one=0

        for i in range(len(nums)+1):
            right = tot - one
            left = i - one
            if i < len(nums) and  nums[i]==1 :
                one+=1
            dic[right + left].append(i)

        return dic[max(dic)]