class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        # redefine the varaibles to be sorted [min->max]

        counter = 0
        # set up the counter for amount of moves

        for x in range(len(seats)):
            counter += abs(seats[x]-students[x])
            # add the amount of moves that the person moved
            # use absolute in the case seats[x]<students[x]
            
        return counter