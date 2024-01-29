# Clue : #All Permutation of given string



class Solution:
    def letterCasePermutation(s):

        res =[]
        slate=[]
        index = 0

        def helper(s, index, slate):

            if index == len(s):
                res.append("".join(slate))
                return
            

            if s[index].isalpha():
                #Upper
                slate.append(s[index].upper())
                helper(s, slate, index+1)
                slate.pop()

                #lower
                slate.append(s[index].lower())
                helper(s, slate, index+1)
                slate.pop()

            else:
                slate.append(s[index])
                helper(s, slate, index+1)
                slate.pop()

            

        

        helper(s, slate, index)
        return res







result = Solution().letterCasePermutation()
print(result)