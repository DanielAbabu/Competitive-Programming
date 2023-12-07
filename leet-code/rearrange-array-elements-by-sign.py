class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
      n=len(nums)
      ans=[0]*n
      posindex=0
      negindex=1
      for i in nums:
          if i<0:
              ans[negindex]=i
              negindex+=2
          else:
              ans[posindex]=i
              posindex+=2
      return ans