

class Solution:
    def fizzBuzz(self, n: int):
        answer = []
        for i in range(1,n):
            if (i % 3 == 0):
                answer.append('Fizz')
            elif (i % 5 == 0 ):
                answer.append('Buzz')
            elif (i % 3 == 0) & (i % 5 == 0):
                answer.append("FizzBuzz")
        
        return answer
    
    
n = 3    
sol = Solution().fizzBuzz(n)
print(sol)