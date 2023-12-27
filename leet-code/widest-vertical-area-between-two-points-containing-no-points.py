class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxm=0
        points.sort()
        for i in range(len(points)-1):
            t=points[i+1][0]-points[i][0]
            maxm=max(maxm,t)
        return maxm