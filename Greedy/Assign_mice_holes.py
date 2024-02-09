#https://www.geeksforgeeks.org/problems/assign-mice-holes3053/1

#assign the mice to the number of holes 


#Write a program to assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

# Input:
# N = 3
# M = {4, -4, 2}
# H = {4, 0, 5}
# Output:
# 4





#User function Template for python3

class Solution:
    def assignMiceHoles(self, N , M , H):

        M.sort()
        H.sort()

        maxTime = 0
        time = 0

        for i in range(0 , N ):
            time += abs(M[i] - H[i])
            maxTime = max(maxTime , time)
            time = 0

        return maxTime
            