class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        M = 10**9+7
        sums = 0
        arr.append(0)
        stack = [-1]
        
        for i2,num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]  
                left = index-stack[-1]
                right = i2-index
                sums += right*left*arr[index]
            stack.append(i2)
            
        return sums%M
        return ans

        