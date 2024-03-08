class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        d = defaultdict(list)
        for i, elem in enumerate(nums):
            d[elem].append(i)
        
        result = [0] * len(nums)
        for indexes in d.values():

            if len(indexes) == 1:
                continue

            lcnt = 0
            ldist = 0
            rcunt = len(indexes)
            rdist = sum(indexes)

            for i in indexes:
                rcunt -= 1
                rdist -= i
                result[i] = ( (lcnt * i - ldist)  +  (rdist - rcunt * i) )
                lcnt += 1
                ldist += i

        return result