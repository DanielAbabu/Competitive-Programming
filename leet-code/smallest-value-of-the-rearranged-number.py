class Solution:
    def smallestNumber(self, num: int) -> int:
        dit={}
        if num ==0:
            return 0

        if num<0:
            s = sorted(list(str(abs(num))), reverse=True)
            return int("".join(s)) * (-1)
        else:
            s = sorted(list(str(num)))
            i=0
            while i <len(s) and s[i] =="0" :
                i+=1
            s[0],s[i]=s[i],s[0]
            return int("".join(s)) 



