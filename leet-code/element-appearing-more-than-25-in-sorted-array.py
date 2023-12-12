class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dif= Counter(arr)
        return max(dif , key= lambda x:dif[x] )
        