class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        times = 1
        add = 0
        for i in range (len(str(n))):
            times *= int(str(n)[i])
            add += int(str(n)[i])
        return times-add
        