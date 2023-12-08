class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        possible = []
        
        for ran in ranges:
            possible.extend(list(range(ran[0],ran[1] + 1)))
            
        possible=set(possible)
        for i in range(left, right + 1):
            if i not in possible:
                return False
        
        return True