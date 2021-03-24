class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        lit=[]
        temp = start
        for i in range (n):
            lit.append(start+2*i)
        for j in range (1,n):
            target = temp^lit[j]
            temp = target
        return temp