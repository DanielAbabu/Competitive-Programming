class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[[0]*len(matrix) for _ in range(len(matrix[0]))]

        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                ans[c][r]=matrix[r][c]
        return ans
