class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        cnt = [0] * n

        for s, e in requests:
            cnt[s] += 1
            if e + 1 < n:
                cnt[e + 1] -= 1
        
        cnt = sorted(accumulate(cnt), reverse=True)
        nums.sort(reverse=True)

        return sum(c * num for c, num in zip(cnt, nums)) % (10 ** 9 + 7)


