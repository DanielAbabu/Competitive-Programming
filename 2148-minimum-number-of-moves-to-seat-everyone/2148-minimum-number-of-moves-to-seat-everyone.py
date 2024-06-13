class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        c = 0

        for x in range(len(seats)):
            c += abs(seats[x]-students[x])
        return c