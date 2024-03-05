class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        buck  = []
        ans = []

        def solve(opens,close):
            if opens == close == n:
                tem = "".join(buck)
                ans.append(tem)
                return

            if opens < n:
                buck.append("(")
                solve(opens+1, close) 
                buck.pop()

            if close < opens:
                buck.append(")")
                solve(opens, close+1) 
                buck.pop()


        solve(0,0)
        return ans