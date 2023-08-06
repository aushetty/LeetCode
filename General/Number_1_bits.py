
#what is a hamming weight
#\https://www.youtube.com/watch?v=yfNPcHY5Wm4

# constraint =  The input must be a binary string of length 32.






n = 00000000000000000000000000001011




class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0 

        while n:
            res += n % 2
            n = n >> 1

        return res






result = Solution().hammingWeight(n)
print(result)