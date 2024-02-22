class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonicstk = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while monotonicstk and temperatures[monotonicstk[-1]] < temperatures[i]:
                ans[monotonicstk[-1]] = i - monotonicstk[-1]
                monotonicstk.pop()

            monotonicstk.append(i)
        
        return ans



