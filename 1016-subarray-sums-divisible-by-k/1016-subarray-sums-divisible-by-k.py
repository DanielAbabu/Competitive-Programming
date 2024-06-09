class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = []
        d = defaultdict(int)
        d[0] = 1
        summ = 0
        ans = 0

        for i in range(len(nums)):
            summ += nums[i]
            pre.append(summ)
        
        for i in range(len(pre)):
            ans += d.get(pre[i] % k, 0)
            d[pre[i] % k] += 1

        return ans