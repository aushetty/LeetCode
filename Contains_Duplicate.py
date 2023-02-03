#Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
nums = [1,1,1,3,3,4,3,2,4,2]


class Solution:
    def containsDuplicate(self, nums) -> bool:
        table = set()
        for num in nums:
            if num in table:
                return True
            else:
                table.add(num)
        return False
    
    
    

result = Solution().containsDuplicate(nums)
print(result)