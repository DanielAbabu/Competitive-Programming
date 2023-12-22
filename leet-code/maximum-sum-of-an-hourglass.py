class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxm=float('-inf')

        for r in range(len(grid)-2):
            for i in range(len(grid[0])-2):
                summ = grid[r][i] + grid[r][i+1] + grid[r][i+2] + grid[r+1][i+1] + grid[r+2][i] + grid[r+2][i+1]+ grid[r+2][i+2]
                maxm = max(maxm,summ)


        return maxm
