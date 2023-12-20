class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r==c:
                    break
                matrix[r][c],matrix[c][r] = matrix[c][r], matrix[r][c]
        w=len(matrix[0])-1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if c== (w+1)//2:
                    break
                matrix[r][c],matrix[r][w-c] = matrix[r][w-c], matrix[r][c]