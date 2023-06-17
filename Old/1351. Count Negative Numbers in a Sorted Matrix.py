from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        negatives = 0
        
        
        for row in  range(row_len):
            for col in range(col_len):
                if grid[row][col]< 0:
                    negatives += 1
        
        return negatives
    
    

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
sol = Solution()
sol.countNegatives(grid)


#Coments
# in this case we are iterating the grid matrix by row and column to get the negative value count 
# the negative here is thecount iterator which increases whrn it enconters the value less than 0
# hence the output is the total count of the negative value in the matrix 
# 
# 


