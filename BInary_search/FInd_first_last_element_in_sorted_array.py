
class Solution:
    def searchRange(self, nums ,target):

        def binsrch(nums,target,leftb):
            l , r = 0 , len(nums) - 1
            i =-1
            while l <= r:
                mid = (l + r)//2

                if  target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid -1
                else:
                    i = mid
                    if leftb:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i

        
        left = binsrch(nums, target, True)
        print(left)
        right = binsrch(nums, target, False)
        print(right)

        return [left, right]

result = Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
print(result)
 
 