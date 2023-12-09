#recursive approach
# def find_sum(n):

#     if n == 1:
#         return n
    
#     return n + find_sum(n-1)

#iterative approach
def find_sum(n):

    sum = 0

    for i in range(1,n+1):
        sum += i
    return sum 




if __name__ == '__main__':
    print(find_sum(7))