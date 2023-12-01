class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary[1:-1]) / float(len(salary)-2))