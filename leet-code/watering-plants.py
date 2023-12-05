class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        cur=0
        for i,ch in enumerate(plants):
            if ch >cur:
                cur=capacity
                step+= i*2
            cur-=ch
            step+=1
        return step