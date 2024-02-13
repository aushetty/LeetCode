
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