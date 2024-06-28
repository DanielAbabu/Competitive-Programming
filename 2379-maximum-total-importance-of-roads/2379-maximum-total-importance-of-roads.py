class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = Counter()

        for ed in roads:
            count.update(ed)

        ans = 0
        count= OrderedDict(count.most_common())
        for k in count:
            # print( k, count[k], n)
            ans += (count[k] * n)
            n -= 1
        
        return ans


