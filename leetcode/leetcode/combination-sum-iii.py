class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        buck = []
        ans = []
 

        def backtrack(i):
            if len(buck)==k and n == sum(buck):
                ans.append(buck[:])
                return

            if n < sum(buck) or len(buck) > k:
                return

            val =None
            for j in range(i,10):
                if val != j:
                    buck.append( j)
                    backtrack(j+1)
                    val = buck.pop()       
        
        backtrack(1)
        return ans