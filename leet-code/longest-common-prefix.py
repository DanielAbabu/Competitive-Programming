class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        temp=""
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return temp
            temp+=first[i]
        return temp


            