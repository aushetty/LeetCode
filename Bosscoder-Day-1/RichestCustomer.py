#https://leetcode.com/problems/richest-customer-wealth/




accounts = [[1,2,3],[3,2,1]]


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        highest_sum = 0

        for i in accounts:
            curr_sum = sum(i)

            if highest_sum < curr_sum:
                highest_sum = curr_sum 


        return highest_sum



result = Solution().maximumWealth()
print(result)
 
 
 