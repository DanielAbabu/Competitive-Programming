class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrow = 1
        hit = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > hit :
                arrow += 1
                hit = points[i][1]

        return arrow

