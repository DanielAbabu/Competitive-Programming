class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j=0,len(people)-1
        c=0

        while i <= j:
            temp = people[i] + people[j]
            if temp <= limit:
                i+=1
                j-=1
                c+=1
            elif people[j] <= limit:
                c+=1
                j-=1
            else:
                j-=1

        return c


