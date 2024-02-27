class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def poww(x,n):
            if n == 0:
                return 1
            
            if n % 2 == 0:
                return poww((x*x)% 1000000007 , n//2) % 1000000007
            else:
                return (poww(x, n-1) * x) % 1000000007
                
        return ((poww(5, (n+1)//2)) * (poww(4, n//2)))  % 1000000007 

        
