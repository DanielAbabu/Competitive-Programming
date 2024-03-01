class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = customers.count("Y")
        n = 0
        minm = y
        ind = 0

        for i in range(len(customers)):

            if customers[i] == "N":
                n += 1
            if customers[i] == "Y":
                y -= 1         

            if n + y < minm:
                minm = n + y
                ind = i+1

        return ind
                


        