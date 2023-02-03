
#what is a hamming weight
#\https://www.youtube.com/watch?v=yfNPcHY5Wm4

# constraint =  The input must be a binary string of length 32.






n = 00000000000000000000000000001011




class Solution:
    def hammingWeight(self, int):
        
        mystr = str(int)
        a = 0
        for i in mystr:
            if i == 1:
                a+= 1

                
            
        
        
        
        
        
        
        return a






result = Solution().hammingWeight(n)
print(result)