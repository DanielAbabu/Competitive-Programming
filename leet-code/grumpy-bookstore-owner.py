class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        summ = cur = maxm = 0
        qq = deque([])

        for i in range(len(grumpy)):
    
            if i >= minutes and grumpy[i-minutes]:
                cur -= customers[i-minutes]

            if grumpy[i]:
                cur += customers[i]

            if not grumpy[i]:
                summ += customers[i]
            maxm = max(maxm,cur)

        return summ + maxm