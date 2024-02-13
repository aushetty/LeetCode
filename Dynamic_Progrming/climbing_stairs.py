# https://leetcode.com/problems/climbing-stairs/description/





# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

#this is a bottom up approach 



class Solution:
    def climbStairs(self, n: int) -> int:
        #we create a data structure for memoization to reduce time complexity
        memo = {}
        def helper(path):
            if path in memo:
                return memo[path]
            if path == 0:
                return 1
            if path < 0:
                return 0
            memo[path]= (helper(path-1)+helper(path-2))
            return memo[path]
        return helper(n)
