class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        p= defaultdict(int)
        ans = 0
        summ = 0
        
        p[0] = 1
        for num in A:
            summ += num
            if summ - S in p:
                ans += p[summ-S]

            p[summ] += 1

        return ans