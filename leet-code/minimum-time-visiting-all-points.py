class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        ans=0
        for i in range(len(points)-1,0,-1):
            ans+=max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))

        return ans

