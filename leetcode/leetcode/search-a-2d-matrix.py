class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix)-1 
        while l <= r:
            m = (l+r)//2

            if matrix[m][0] > target:
                r = m-1 
            else:
                l = m+1
        
        if r == -1:
            return False
        
        mat = matrix[r]
        l, r = 0, len(mat)-1 
        while l <= r:
            m = (l+r)//2

            if mat[m] > target:
                r = m-1 
            else:
                l = m+1
        
        if r == -1:
            return False
        
        return mat[r] == target