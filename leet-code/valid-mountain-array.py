class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        t=True
        if len(arr)==1:
            return False

        if arr[0]>= arr[1]:
            return False
        if arr[-1]>= arr[-2]:
            return False

        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                t=False
            if not t and arr[i] <= arr[i+1]:
                return False

        return True