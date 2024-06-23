class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mdq = deque()
        miq = deque()

        l, r = 0, 0
        maxm = 0

        while r < len(nums):
            while mdq and nums[r] > mdq[-1]:
                mdq.pop()
            mdq.append(nums[r])

            while miq and nums[r] < miq[-1]:
                miq.pop()
            miq.append(nums[r])

            
            while mdq[0] - miq[0] > limit:
                if mdq[0] == nums[l]: mdq.popleft()
                if miq[0] == nums[l]: miq.popleft()
                l += 1

            maxm = max(maxm, r - l + 1)
            r += 1
        return maxm
