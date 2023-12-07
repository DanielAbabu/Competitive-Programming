class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        dist=[0]*len(boxes)
        for i in range(len(boxes)):
          for j in range(len(boxes)):
            
            if boxes[j] =="1" and j!=i:
              dist[i]+=abs(j-i)
        return dist