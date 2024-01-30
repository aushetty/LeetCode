
# https://leetcode.com/problems/subsets-ii/description/

# Clue:   (Power set)used back tracking



class Solution:
    def subsetsWithDup(self,nums):

        res = []
        nums.sort()



        def backtrack(i, subset):

            if i == len(nums):

                res.append(subset[::])
                return

            #all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()


            #all subsets that does not include nums[i]





    