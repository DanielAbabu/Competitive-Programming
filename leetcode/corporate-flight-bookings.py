class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0]*(n+1)

        for book in bookings:
            pre[book[0]-1] += book[2]
            pre[book[1]] += -1*book[2]
        
        for i in range(1,n+1):
            pre[i] += pre[i-1]
            
        return pre[:-1]


        