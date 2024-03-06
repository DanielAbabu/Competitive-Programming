class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        def nearest(house): 
            l = 0
            r = len(heaters) -1
            

            while l  <=  r:
                m = (l+r)//2

                if heaters[m] >= house:
                    r = m -1
                else:
                    l = m + 1


            # print(heaters[l], l, heaters[m], r)
            if r == -1:
                r = 0

            if l == len(heaters):
                l = len(heaters)-1
            return min( abs(heaters[l] - house), abs(heaters[r] - house) )
        
        ans = []
        for house in houses:
            rad = nearest(house)
            ans.append(rad)

        # print(ans)
        return max(ans)
        

