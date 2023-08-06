#https://www.youtube.com/watch?v=T41rL0L3Pnw

matrix = [[1,1,1],[1,0,1],[1,1,1]]

class Solution:
    def setZeroes():
        
        rows, cols = len(matrix) , len(matrix[0])
        rowZero = False
        
    #determine wich rows and cols need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if  r > 0 :
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
                
                
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

result = Solution().setZeroes()
print(result)