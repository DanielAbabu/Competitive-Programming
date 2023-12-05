class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        di=sum(distance[min(start,destination):max(start,destination)])
        tot=sum(distance)
        return min(tot-di,di)