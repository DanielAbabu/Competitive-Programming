class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, len(arr)-1
        while l <= r:
            m = (l+r)//2
            if arr[m] >= x:
                r = m-1
            else:
                l = m+1

        l = max(0, l)
        print(l)
        if l >= len(arr):
            l = len(arr)-1

        if x != arr[l]:
            l = max(0, l-1)
        r = l+1

        while k:
            
            if l > -1 and r < len(arr):
                if abs(x - arr[l]) > abs(x - arr[r]):
                    r += 1
                else:
                    l -= 1
            elif l > -1 and r > len(arr)-1:
                l -= 1
            elif l < 0 and r < len(arr):
                r += 1
            else:
                l = 0
                r = len(arr)
                break
            k-=1
        l+=1
        if l < 0:
            l =0
        

        ans = arr[l:r]
        return ans