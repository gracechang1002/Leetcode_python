class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a_int = int(a,2)
        b_int = int(b,2)
        output = bin(a_int+b_int)[2:]
        return output