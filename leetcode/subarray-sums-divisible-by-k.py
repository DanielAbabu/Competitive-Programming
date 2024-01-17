class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = []
        dic = defaultdict(int)
        dic[0] = 1
        summ = ans = 0

        for i in range(len(nums)):
            summ += nums[i]
            pre.append(summ)
        
        for i in range(len(pre)):
            ans += dic.get(pre[i]%k, 0)
            dic[pre[i]%k] += 1

        return ans