#Leetcode video for reference
#https://www.youtube.com/watch?v=DEJAZBq0FDA



class Solution:
    def removeDuplicates(self, nums): 
        l = 1
    
        
        for r in range (1, len(nums)):
            if nums[r]  !=  nums[r-1]:
                nums[l] = nums[r]
                l += 1
            else:
                nums[r] == " "
                
        
        return l
        
        
        
        
        
        
        
        
nums = [0,0,1,1,1,2,2,3,3,4]

result = Solution()
k = result.removeDuplicates(nums)
print(k)

