#Leetcode video for reference
#


class Solution:
    def maxProfit(self, prices) -> int:
        
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i-1])
                
        return profit
        
prices = [7,1,5,3,6,4]

result = Solution()
k = result.maxProfit(prices)
print(k)

