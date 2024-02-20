class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        a = b = len(costs)/2
        costs.sort( key = lambda x : -abs(x[0] - x[1]))  

        for cost in costs:
            if b == 0 or (cost[0] < cost[1] and a > 0):
                ans += cost[0]
                a -= 1
            else:
                ans += cost[1]
                b -= 1
        
        return ans
