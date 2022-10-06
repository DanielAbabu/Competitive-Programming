class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []  
        for x in range(1,n+1):
            list=''
            if x % 3 == 0:
                list += 'Fizz'
            if x % 5 == 0:
                list+='Buzz'
            if x % 3 != 0 and x % 5 !=0:
                list += str(x)
            res.append(list)
        return res