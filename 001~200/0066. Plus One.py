class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        numm = 0
        numm = int(''.join(str(i) for i in digits))
        digits = [int(i) for i in str(numm+1)]
        return digits
        