#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
nums = [4,1,2,1,2]

class Solution:
    def singleNumber(self, nums) -> int:
        
        s = set()
        for i in nums:
            if i in s: 
                s.remove(i)
            else: 
                s.add(i)
    
        return str(s)
        
        

result = Solution().singleNumber(nums)
print(result)