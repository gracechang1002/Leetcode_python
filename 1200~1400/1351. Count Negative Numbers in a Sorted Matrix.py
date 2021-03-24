class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        numcol = len(grid)
        numrow = len(grid[0])
        temp = 0
        
        for i in range (numcol):
            for j in range (numrow):
                if grid[i][j]<0:
                    temp+=1
        return temp