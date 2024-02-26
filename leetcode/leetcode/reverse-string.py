class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reversing(i):
            if i == len(s)//2: return
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

            return reversing(i+1)
        
        reversing(0)
        
        


