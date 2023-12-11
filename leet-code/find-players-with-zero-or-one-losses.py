class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        outcome=defaultdict(int)
        for match in matches:
            outcome[match[0]] = outcome.get(match[0],0)
            outcome[match[1]] += 1
        ans=[[],[]]
        for key,value in outcome.items():
            if value == 0:
                ans[0].append(key)
            elif value == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans

