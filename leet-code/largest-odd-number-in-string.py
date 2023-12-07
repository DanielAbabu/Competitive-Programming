class Solution:
    def largestOddNumber(self, num: str) -> str:
        num=list(num)
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) %2 !=0:
                return "".join(num[:i+1])
        return ""