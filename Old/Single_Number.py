#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
nums = [4,1,2,1,2,3,4,5,3]

class Solution:
    def singleNumber(self, nums) -> int:
        
        # result = 0
        # for i in arr:
        #     result ^= i
        # return result
        #Bit manipulation technique
        # refer https://www.google.com/search?q=++Single+Number+python&client=firefox-b-d&ei=1r6HZJL5PK6MseMPxOClgA4&ved=0ahUKEwiSvPD9hL__AhUuRmwGHURwCeAQ4dUDCA4&uact=5&oq=++Single+Number+python&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46CggAEEcQ1gQQsAM6BwgAEIAEEAo6CAgAEIoFEIYDSgQIQRgAUNoDWJsQYLESaANwAXgAgAFuiAGVBpIBAzUuM5gBAKABAqABAcABAcgBCA&sclient=gws-wiz-serp#fpstate=ive&vld=cid:36e9b9b8,vid:qMPX1AOa83k
        # xor two values that are same and compare
        

        
        print(set(nums))
        print(2*sum(set(nums)))
        
    
        return 2*sum(set(nums)) - sum(nums)
        
        

result = Solution().singleNumber(nums)
print(result)