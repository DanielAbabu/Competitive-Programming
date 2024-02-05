class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        pre = [[0] * m for _ in range(n)]

        for j in range(m):
            pre[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(m):
                pre[i][j] = pre[i - 1][j] + matrix[i][j]
        

        def getSum(r1, r2, c):
            if r1 == 0:
                return pre[r2][c]
            else:
                return pre[r2][c] - pre[r1 - 1][c]

        def getForRows(r1, r2):
            sums = Counter()
            curSum = 0
            cc = 0

            for c in range(m):
                curSum += getSum(r1, r2, c)
                if curSum == target:
                    cc += 1
                if curSum - target in sums:
                    cc += sums[curSum - target]
                sums[curSum] += 1  
            return cc 

        cc = 0
        for r1 in range(n):
            for r2 in range(r1, n):
                cc += getForRows(r1, r2)     
        return cc