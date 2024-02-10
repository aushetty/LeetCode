

#https://leetcode.com/problems/fibonacci-number/




#recursive approach
def find_sum(n):

    if n == 1:
        return n
    
    return n + find_sum(n-1)

#iterative approach
# def find_sum(n):

#     sum = 0

#     for i in range(1,n+1):
#         sum += i
#     return sum 



#fibonacci series

def fib(n):


    if n == 0 or n == 1:
        return n 
    
    
    return fib(n-1) + fib(n-2)





# class Solution:
#     def fib(self, n: int) -> int:
#         memo = [-1]*(n+1)
#         def helper(n):
#             nonlocal memo
#             if n == 0 or n == 1:
#                 return n  
#             if memo[n] != -1:
#                 return memo[n]
#             memo[n] = helper(n-1) + helper(n-2)
#             return memo[n]
#         return helper(n)



if __name__ == '__main__':
    print(find_sum(7))
    print(fib(5))