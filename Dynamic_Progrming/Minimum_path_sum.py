# https://leetcode.com/problems/minimum-path-sum/description/








class Solution:
    def minPathSum(self, grid) -> int:
        
        #initialize a grid
        m = len(grid)
        n = len(grid[0])

        memo = {}
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i >= m or j >=n:
                return float("inf")

            if i == m-1 and j == n-1:
                return grid[i][j]
            
            memo[(i,j)] = grid[i][j]+ min(helper(i, j+1), helper(i+1, j))
            return memo[(i,j)]
        return helper(0,0)
    



