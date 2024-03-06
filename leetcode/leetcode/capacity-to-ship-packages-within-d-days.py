class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)

        def day(cap):
            d = 1
            tem = 0

            for i in range(len(weights)):
                if tem + weights[i] > cap:
                    d += 1
                    tem = weights[i]
                else:
                    tem += weights[i]
            return d

        
        while l < r:
            m = (l+r)//2

            if day(m) <= days:
                r = m
            else:
                l = m+1
        
        return l





 

        print(day)
        return max(day)

        