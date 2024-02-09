#https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

# Consider that all the trains arrive on the same day and leave on the same day. 
# Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. 
# At any given instance of time, 
# same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.




# Input: n = 6 
# arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
# dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
# Output: 3



# recalling Notes:

# 1. sort the arriveal and departure , dont care about which train is arriving or leaving , just remember at the given departure time 
# one of the train will definitely leave , so dont bother about the platform 








#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):

        arr.sort()
        dep.sort()


        #Initialize values first 

        platform_needed = 0
        max_platforms = 0


    #This is also the start point and the endpoint , two pointers for both the arrays 
        i = 1
        j = 0


        while i < n and j < n:
            # If next event is arrival, increase the count of trains at station
            if arr[i] < dep[j]:
                platform_needed += 1
                i += 1
                 # Update max platforms needed
                max_platforms = max(platform_needed , max_platforms)

            # If next event is departure, decrease the count of trains at station
            elif arr[i] >= dep[j]:
                platform_needed -= 1
                j += 1

        return max_platforms