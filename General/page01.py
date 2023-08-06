n = [1,15,13,8]

def maxcheck(n):
    max = 0 

    for i in range(0,n):
        for j in range(1+1 , n):
            val = |n[i] - n[j]| + |i-j|
            
            if val > max:
                max = val
                
                
    return max




