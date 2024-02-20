class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = defaultdict(int)
        for i,c in enumerate(s):
            h[c] = i
        last = -1
        maxm =  0
        ans = []        
        for i,c in enumerate(s):
            maxm = max(maxm,h[c])
            if maxm == i:
                ans.append(i - last)
                last =i

        return ans



