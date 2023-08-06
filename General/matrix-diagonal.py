mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

#https://leetcode.com/problems/matrix-diagonal-sum/



class Solution:
    def diagonalSum(self):
        
        res , n = 0 , len(mat)
        
        for i in range(0, n):
            res += mat[i][i]  #first diagonal
            res += mat[i][n -1 -i]  
        
        return res - (mat[n //2][n//2] if n % 2 else 0)      
        







result = Solution().diagonalSum()
print(result)



