class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        output = 0
        
        while n !=1:
            output+= n // 2
            n = n - n//2

        return output