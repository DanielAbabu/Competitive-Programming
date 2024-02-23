class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for num in nums:
            if stk and num == stk[-1]:
                stk.pop()
                ans += 1
            
            stk.append(num)
            if len(stk) == 2:
                stk = []

        return ans + len(stk)