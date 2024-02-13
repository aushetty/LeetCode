
#https://www.geeksforgeeks.org/problems/friends-pairing-problem5425/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab



# Notes

# Ah, I see! Let's incorporate the formula (n−1)
# (n−1) into the problem.
# Suppose we have 4 friends (A, B, C, D) again. We want to either pair them up or let them remain single.
# Now, let's say we first decide to pair friend A with one of the remaining friends (B, C, or D). After selecting A's partner, we are left with 3 friends (B, C, D) to form pairs or remain single.
# For each choice of A's partner, there are (n−1)
# (n−1) possibilities, where n
# n is the number of friends remaining. This is because A can be paired up with any of the remaining (n−1)
# (n−1) friends.
# So, considering friend A as the first friend to be paired up, there are (n−1)
# (n−1) ways to select A's partner, and then there are countFriendsPairings(n−2)
# countFriendsPairings(n−2) ways to pair up the remaining (n−2)
# (n−2) friends.
# This is why we use the formula (n−1)×countFriendsPairings(n−2)
# (n−1)×countFriendsPairings(n−2) in the recursive solution. It accounts for the number of choices for the first friend to pair up, multiplied by the number of ways to handle the remaining friends.
# So, in the example with 4 friends:
# countFriendsPairings(4)=(4−1)×countFriendsPairings(3)
# countFriendsPairings(4)=(4−1)×countFriendsPairings(3)
# This represents the number of ways to pair up or remain single for 4 friends, where the first friend can be paired up with any of the remaining 3 friends, and then the remaining 3 friends are handled recursively.
# I hope this clarifies how the formula (n−1)
# (n−1) fits into the combination problem! Let me know if you have further questions!



class Solution:
    def countFriendsPairings(self, n):
        MOD = 10**9 + 7
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1
            if n < 0:
                return 0
            
            memo[n] = (self.countFriendsPairings(n-1) + (self.countFriendsPairings(n-2) * (n-1))) % MOD
            return memo[n]

        return helper(n)
    





# For similar problems refer this link for practice
# https://www.geeksforgeeks.org/number-of-ways-to-pair-people/#practice




# Iterative approach
    

#NOte for iterative approach 
    

#understand how we arrived at the formula 
#if a , b, c,d are the elements we need to find combination of pairing then within the dp array find the value for (i-1)th element and (i-2)th element 
    





class Solution:
    def countFriendsPairings(self, n):
        MOD = 10**9 + 7

        dp = [0] * (n+1)

        #here we populated the 0th and 1st indexes because the return value for 0 remaining element and 1 remaining element is 1, hence dp[0] and dp[1] is 1 
        dp[0] = 1
        dp[1] = 1

        #now we iterate the loop from position 2 to n+1 and use the above logic of sum of hop of i-1 and i-2 positions alongwith * (i-1) to calculate all possible combinations for the elements
        
        for i in range(2 , n+1):
            dp[i] = (dp[i-1] + (dp[i-2] * (i-1))) % MOD


        return dp[n]



    