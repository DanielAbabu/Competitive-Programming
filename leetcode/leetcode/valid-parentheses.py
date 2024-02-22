class Solution:
    def isValid(self, s: str) -> bool:
        sta=[]
        h = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in {'(', '{', '['}:
                sta.append(i)
            else:
                if sta and h[sta[-1]] == i:
                    sta.pop()
                else:
                    return False
        
        return False if sta else True 
