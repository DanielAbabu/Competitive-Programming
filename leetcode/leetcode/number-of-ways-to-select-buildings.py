class Solution:
    def numberOfWays(self, s: str) -> int:
        dic = {"01":0, "10":0}
        zeros = ones = ans = 0

        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
                dic["01"] += zeros
                ans += dic["10"]
            else:
                zeros += 1
                dic["10"] += ones
                ans += dic["01"]

        return ans
