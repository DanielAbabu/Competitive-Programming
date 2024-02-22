class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        sta = []

        for i in path:
            if i not in {"",".",".."}:
                sta.append(i)
            elif i == ".." and sta:
                sta.pop()
        
        return "/" + "/".join(sta)
