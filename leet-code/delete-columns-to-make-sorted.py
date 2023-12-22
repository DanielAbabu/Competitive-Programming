class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j+1][i] < strs[j][i]:
                    c+=1
                    break
        return c
