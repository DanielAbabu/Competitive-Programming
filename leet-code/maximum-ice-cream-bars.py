class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cost = dict(Counter(costs))
        costs = sorted(cost, key=lambda x:x)
        ans=0
        for i in costs:
            if coins < i:
                return ans
            else:
                if coins - (cost[i] * i) >= 0:
                    coins-= (cost[i] * i)
                    ans += cost[i]
                else: 
                    ans += coins//i
                    return ans

        return ans

        