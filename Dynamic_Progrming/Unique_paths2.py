# https://leetcode.com/problems/unique-paths-ii/




class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        #comversion of obstacle grid into rows and columns 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

    
        #similar solution like unique paths 1 
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i > m-1 or j > n-1 or obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            memo[(i,j)] = helper(i,j+1) + helper(i+1, j)
            return  memo[(i,j)]

        return helper(0,0)
        