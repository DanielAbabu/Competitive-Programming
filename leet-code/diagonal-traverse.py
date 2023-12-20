class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]
        tem=defaultdict(list)
        c,r=0,0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                tem[c+r].append(mat[r][c])

        for key,value in tem.items():
            if key%2!=0:
                ans.extend(value)
            else:
                ans.extend(value[::-1])
        return ans