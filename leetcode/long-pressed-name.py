class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        i = 0
        for t in range(len(typed)):
            if i < n and name[i] == typed[t]:
                i += 1

            elif t == 0 or typed[t] != typed[t - 1]:
                return False

        return i == n 


        