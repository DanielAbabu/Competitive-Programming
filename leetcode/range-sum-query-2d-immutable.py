class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r,c = len(matrix), len(matrix[0])
        self.arr = [[0]*(c+1) for i in range(r+1)]

        for i in range(r):
            for j in range(c):
                self.arr[i+1][j+1] = self.arr[i+1][j] + self.arr[i][j+1] + matrix[i][j] - self.arr[i][j]
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        col1+=1
        col2+=1
        row1+=1
        row2 +=1
        return self.arr[row2][col2] - self.arr[row2][col1 -1] -self.arr[row1 - 1][col2] + self.arr[row1 -1][col1 -1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)