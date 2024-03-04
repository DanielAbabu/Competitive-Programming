class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        buck = []
        def backtrack(i):
            if len(buck) == k:
                ans.append(buck.copy())
                return

            for j in range(i+1,n+1):
                buck.append(j)
                backtrack(j)
                buck.pop()
            
        backtrack(0)
        return ans

