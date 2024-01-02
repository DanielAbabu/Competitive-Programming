import copy
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat=[]
        for _ in range(m):
            tem=[]
            for j in range(n):
                tem.append("c")
            mat.append(tem)

        for g in guards:
            mat[g[0]][g[1]]="g"

        for w in walls:
            mat[w[0]][w[1]]="w"
        
        tem = copy.deepcopy(mat)

        for i in range(m):
            c=0
            see=False
            for j in range(n):
                c+=1
                if see and mat[i][j] != "w":
                    mat[i][j] = "m"

                elif mat[i][j] == "g":
                    for b in range(j-1,j-c,-1):
                        mat[i][b] = "m"
                    see=True
                    c=0

                elif see and mat[i][j] == "w":
                    mat[i][j] = "m"
                    see=False
                    c=0

                elif mat[i][j] == "w":
                    c=0

        for j in range(n):
            c=0
            see=False
            for i in range(m):
                c+=1
                if see and tem[i][j] != "w":
                    mat[i][j] = "m"

                elif tem[i][j] == "g":
                    for b in range(i,i-c,-1):
                        mat[b][j] = "m"
                    see=True
                    c=0

                elif see and tem[i][j] == "w":
                    mat[i][j] = "m"
                    see=False
                    c=0

                elif tem[i][j] == "w":
                    c=0


        ans=0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "c":
                    ans+=1
        

        return ans