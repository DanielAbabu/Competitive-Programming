class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(None)
        ans = []
        j = 0
        for i, ch in enumerate(s):
            if i == spaces[j]:
                j += 1
                ans.append(" ")
            ans.append(ch)
        return "".join(ans)