class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        ans = []
        
        for i in range(x):
            maxm = max(arr[:x - i])
            max_i = arr.index(maxm) + 1
            arr[:max_i] = reversed(arr[:max_i])
            ans.append(max_i)
            
            arr[:x - i] = reversed(arr[:x - i])
            ans.append(x - i)
        return ans