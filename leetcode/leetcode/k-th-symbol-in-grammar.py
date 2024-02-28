class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def grammer(k):
            if k == 1:
                return 0
            
            
            nearest = 2**(floor(log(k,2)))
            print(nearest,k)
            if k == nearest:
                if (floor(log(k,2)))%2==1:
                    return 1
                else:
                    return 0
            val = grammer(k%nearest)
            
            if val == 0:
                return 1
            else:
                return 0
        return grammer(k)

        