class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        aqueue = deque()
        bqueue = deque()

        l, r = 0, 0
        maxm = 0
        while r < len(nums):
            while aqueue and nums[r] > aqueue[-1]:
                aqueue.pop()
            aqueue.append(nums[r])

            while bqueue and nums[r] < bqueue[-1]:
                bqueue.pop()
            bqueue.append(nums[r])

            
            while aqueue[0] - bqueue[0] > limit:
                if aqueue[0] == nums[l]: aqueue.popleft()
                if bqueue[0] == nums[l]: bqueue.popleft()
                l += 1

            maxm = max(maxm, r - l + 1)
            r += 1
        return maxm
