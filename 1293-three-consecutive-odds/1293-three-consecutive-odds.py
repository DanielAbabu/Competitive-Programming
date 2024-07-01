class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        od = 0
        for a in arr:
            if a & 1:
                od += 1
            else:
                od = 0
            if od == 3:
                return True 
        return False