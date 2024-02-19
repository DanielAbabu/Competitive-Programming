class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        n = len(s)//4
        res = len(s)
        i = 0

        for j, c in enumerate(s):
            count[c] -= 1

            while i < len(s) and count['Q'] <= n and count['W'] <= n and count['E'] <= n and count['R'] <= n:
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1

        return res

            