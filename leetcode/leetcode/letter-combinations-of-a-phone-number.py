class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = []
        s = []
        def backtrack(i):
            if len(s) == len(digits):
                tem = "".join(s)
                if tem != "":
                    ans.append(tem)
                return
            
            ss = d[digits[i]]
            for j in range(len(ss)):
                s.append(ss[j])
                backtrack(i+1)
                s.pop()
        
        backtrack(0)
        return ans
            
