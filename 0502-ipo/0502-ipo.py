class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap = []
        j = 0
        arr = list(zip(capital,profits))
        arr.sort()

        for i in range(k):
            
            while j < len(profits) and w >= arr[j][0]:
                heappush(maxheap,-(arr[j][1]))
                j += 1

            if not maxheap:
                break

            else:
                w += -(heappop(maxheap))

        return w
