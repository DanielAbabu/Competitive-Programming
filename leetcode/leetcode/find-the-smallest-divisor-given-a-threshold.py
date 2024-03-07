class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        


        def find(v):
            tot = 0
            for num in nums:
                tot += math.ceil(num/v)
            print("t",tot)
            return tot
        l = 1
        r = max(nums)+1

        while l <= r:
            
            m = ( l+r )//2
            if find(m) <= threshold:
                r = m-1
            else:
                l = m+1
        
        return l
