class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid = [[0]*len(colSum) for i in range(len(rowSum))]

        for r in range(len(rowSum)):
            for c in range(len(colSum)):
                grid[r][c] = max(min(rowSum[r], colSum[c]),0)
                rowSum[r] -= grid[r][c]
                colSum[c] -= grid[r][c]
        return grid