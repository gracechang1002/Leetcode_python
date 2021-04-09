class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
         
        output = [0]*numRows
        
        for i in range (numRows):
            row = [0]*(i+1)
            if i<=1:
                for j in range (i+1):
                    row[j] = 1
                    output[i] = row
            else:
                row[0] = 1
                row[i] = 1
                for k in range (1,i):
                    row[k] = output[i-1][k-1]+output[i-1][k]
                output[i] = row
        return output