class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        tem = sorted(intervals)
        d = {}
        for i in range(len(intervals)):
            d[intervals[i][0]] = i

        
        def find(val):
            l = 0
            r = len(intervals)-1

            while l <= r:
                m = (l+r)//2

                if  tem[m][0] >= val:
                    r = m - 1
                else:
                    l = m + 1

            if l == len(tem):
                l -= 1

            if r == -1:
                r = 0


            return d.get(tem[l][0]) if tem[l][0] >= val else -1

        ans = []
        for i in range(len(intervals)):
            position = find(intervals[i][1])

            if position == -1:
                ans.append(-1)
            else:
                ans.append(position)
                


        return ans