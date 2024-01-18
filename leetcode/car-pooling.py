class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger = [0]*1002

        for trip in trips:
            passenger[trip[1]] += trip[0]
            passenger[trip[2]] -= trip[0]


        for i in range(1,1002):
            passenger[i] += passenger[i-1]
            if passenger[i-1] > capacity:
                return False
            
        return True