#Leetcode video for reference
#https://www.youtube.com/watch?v=1pkOgXD63yU

class Solution:
    def maxProfit(self, prices) -> int:
        #initialize pointers
        #l=left=buying
        #r=right=selling
        l,r = 0,1
        maxP = 0
        
        while r < len(prices):
            #checking profitability
            if prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    maxP = max(maxP , profit)
            else:
                l = r
            
            r+=1
        return maxP
        

prices = [7,1,5,3,6,4]
