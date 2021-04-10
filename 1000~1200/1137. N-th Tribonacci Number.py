class Solution:
    def tribonacci(self, n: int) -> int:
        
        output = [0,1,1]
        if n < 2:
            return output[n]
        
        for i in range (n-2):
            output.append(sum(output))
            output.pop(0)
        return output[-1]