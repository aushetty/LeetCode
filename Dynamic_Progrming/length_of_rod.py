#https://www.geeksforgeeks.org/problems/rod-cutting0840/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article


# Determine the maximum value obtainable by cutting up the rod and selling the pieces.

#We are using a bottom-up i.e iterative approach to solve the problem 
#In this method we initialize a array for memoization with zero value 
# We create a max_profit variable with a float"-inf" value and then populate it with the comparison of max value of profit from the length of rod i.e N to the cut made from the rod 
#Note that the price array is given on 1 based indexing with the price of profit for 1 cut of the rod as 1 , 2 cut of the rod as 5 , 3 as 8 ....so on

#  Input:
# N = 8
# Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
# Expected Output:
# 22


class Solution:

    def cutRod(self, n , price):

        # we create an empty array for memoization where the value for the max profit will be populated based on the cut of the rod 
        #populate array with 0 based indexing [0,0,0,0,0,0,0,0,0] for now
        dp = [0] * (n+1)


        #Iterate over the entire length of the rod , from 1 to length of rod with 1 based indexing , i.e incase of n=8 (1, 9) ===> 1,2,3.....8 cuts
        for length in range (1 , n+1):
            #we create a variable of max profit to compare and assign the most minimum value to it  as the worst case scenario
            max_profit = float('-inf')
            # iterate over all possible cuts for the current length chosen in the above loop and update the maximum value 
            for cut in range(1, length+ 1):
                #comparison to achieve max value between  maximum profit value initialized  with the sum(price of each cut from the [for loop with the previous value] and 
                # value from the dp array of the corresponding cut )

                #we arrive at this formula by understanding that maximum profit can  be determined if we compare a 
                #predefined max_profit value with the price of cut for the least rod length and travel upwards from that point to the length of the rod
                #For eg: for length=8 , range(1,8) first iteration length=1 and cut=1 
                #max_profit = max(-999, price[1-1]+dp[1-1]) which is max_profit = max(-999, 1+0) likewise  the "cut" for loop will run length times to derive the max value for that cut and eventually 
                # that value is stored and returned in dp[length ] = max_profit

                max_profit = max(max_profit, price[cut-1]+dp[length-cut])
            #storing max value from the cut derived after length iterations
            dp[length] = max_profit


        return dp[n]


