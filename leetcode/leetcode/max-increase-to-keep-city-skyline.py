class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxm = [0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxm[j] = max(maxm[j], grid[i][j])

        ans = 0
        for i in range(len(grid)):
            row = max(grid[i])
            for j in range(len(grid[i])):
                pos = min(row, maxm[j])

                ans += max(pos - grid[i][j],0)
        
        return ans

