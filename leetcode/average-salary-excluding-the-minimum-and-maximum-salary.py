class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary[:] = salary[1:-1]
        n = len(salary)

        return sum(salary)/n 
        