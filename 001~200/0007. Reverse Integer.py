class Solution:
    def reverse(self, x: int) -> int:
        
        ch = []
        if x > 0:
            for i in range (len(str(x)),0,-1):
                ch.append(str(x)[i-1])
            if int(''.join(str(i) for i in ch)) > 2**31-1:
                return 0
            else:
                return int(''.join(str(i) for i in ch))
            
        
        elif x < 0:
            for i in range (len(str(x)),1,-1):
                ch.append(str(x)[i-1])
            if int(''.join(str(i) for i in ch))*-1 < -2**31:
                return 0
            else:
                return int(''.join(str(i) for i in ch))*-1
        
        else:
            return 0
    