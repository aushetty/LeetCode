from typing import List
 
class Solution:
    def findMedian(self, matrix: List[List[int]]) -> bool:
        
        if len(matrix) == 1:
            vec = matrix[0]
            return vec[len(vec) // 2]
        else:
            new_list = []
            for row in range(len(matrix)):
                new_list.extend(matrix[row])
            new_list.sort()    
        
        return new_list[len(new_list) // 2]
    
    
    
    
    
matrix = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]] 
    
sol = Solution()
res = sol.findMedian(matrix)
print(res)

     