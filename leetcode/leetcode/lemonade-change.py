class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = {5:0, 10:0, 20:0}


        for bill in bills:

            c[bill] += 1
            if bill == 10:
                if c[5] == 0:
                    return False
                c[5] -= 1

            elif bill == 20:
                if (c[5] == 0 and c[10] == 0) or  c[5] == 0 :
                    return False

                elif c[10] == 0 :
                    if c[5] < 3:
                        return False
                    c[5] -= 3 
                else:
                    c[5] -= 1 
                    c[10] -= 1  


        return True    


