#https://leetcode.com/problems/combination-sum/

#Follow Akshats style


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        slate = []
        curr_sum = 0
        index = 0


        def helper(slate, curr_sum, index):
            if curr_sum == target:
                return (res.append(slate[::]))

            elif curr_sum > target:
                return

            for i in range(index , len(candidates)):
                slate.append(candidates[i])
                helper(slate , curr_sum + candidates[i] , i )
                slate.pop()


        helper(slate , curr_sum , index)


        return res


