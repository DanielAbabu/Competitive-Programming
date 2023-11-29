class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strings=''
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[i-1][j]:
                    return strings
            strings+=strs[0][j]
        return strings