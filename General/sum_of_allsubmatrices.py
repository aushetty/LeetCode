arr = [[ 1, 1, 1 ],
        [ 1, 1, 1 ],
        [ 1, 1, 1 ]]



n = 3




# def matrixSumm(n , arr):
    
#     sum = 0
    
    
#     for i in range(n) :
#         for  j in range(n):
            
#             top_left = (i+1) * (j+1)
#             bottom_right = (n - i) * (n - j)
            
            
            
#             sum += (top_left * bottom_right * arr[i][j])
            
            
#     return sum


def matrixSum(arr) :
     
    # Variable to store the required sum
    sum = 0
 
    # Nested loop to find the number of
    # submatrices, each number belongs to
    for i in range(n) :
        for j in range(n) :
 
            # Number of ways to choose
            # from top-left elements
            top_left = (i + 1) * (j + 1)
            print("the TLis :",top_left)
 
            # Number of ways to choose
            # from bottom-right elements
            bottom_right = (n - i) * (n - j)
            
            print("the BRis :",bottom_right)
            
            sum += (top_left * bottom_right *
                                  arr[i][j])
            
            print("the corresponding sum is :",sum)
 
    return sum






print(matrixSum(arr))