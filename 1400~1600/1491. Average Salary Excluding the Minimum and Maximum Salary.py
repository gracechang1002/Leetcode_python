class Solution:
    def average(self, salary: List[int]) -> float:
        
        avg = 0
        
        salary.remove(max(salary),)
        salary.remove(min(salary))

        avg = sum(salary) / len(salary)
        return avg