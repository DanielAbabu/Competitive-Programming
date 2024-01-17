class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = [0]
        
        summ = ans = 0

        for num in nums:
            summ += num
            pre.append(summ)



        for i in range(1,len(pre)):
            if pre[i] == pre[-1]-pre[i-1]:
                return i-1
        return -1
        