class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        j = 0
        win = blocks[:k]
        c = minm = win.count("W")

        for i in range(k,len(blocks)):
            if blocks[i] == "W":
                c += 1
            if blocks[i-k] == "W":
                c -= 1
            
            minm = min(minm, c)
        
        return minm