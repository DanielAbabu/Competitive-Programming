class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        S = sum(nums)
        R = S % p
        if R == 0:
            return 0

        pre = 0
        rel = {0: -1}
        ans = len(nums)
        for i, v in enumerate(nums):
            pre = (pre + v) % p
            r = (pre - R) % p
            if r in rel:
                j = rel[r]
                ans = min(ans, i - j)
            rel[pre] = i

        return ans if ans < len(nums) else -1