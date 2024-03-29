class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        buck = []
        ans = []
        candidates.sort()

        def backtrack(i):
            if target == sum(buck):
                ans.append(buck[:])
                return

            if target < sum(buck):
                return

            val =None
            for j in range(i,len(candidates)):
                if val != candidates[j]:
                    buck.append( candidates[j] )
                    backtrack(j+1)
                    val = buck.pop()       
        
        backtrack(0)
        return ans