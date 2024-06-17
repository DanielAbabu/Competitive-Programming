class Solution:
   def judgeSquareSum(self, c: int) -> bool:
        i , j = 0 , int(sqrt(c))
        while i <= j:
            if i * i + j *j == c:
                return True
            if i * i + j * j >  c :
                j -= 1
            else:
                i += 1
        return False