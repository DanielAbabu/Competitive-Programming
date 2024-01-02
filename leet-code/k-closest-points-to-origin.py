class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: abs(x[0])**2 + abs(x[1])**2)
        return points[:k]
        