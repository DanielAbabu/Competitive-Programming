class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk=[0]
        for brac in s:
            if brac == "(":
                stk.append(0)
            else:
                v=max(2*stk.pop(),1)
                stk[-1]+=v

        return stk[-1]
