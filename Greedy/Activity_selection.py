#https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

# Somewhat related to recursion and backtracking
#ALso refere kadane's algorithm i.e Maximum subarray problem in leetcode


# Input:
# N = 2
# start[] = {2, 1}
# end[] = {2, 2}
# Output: 
# 1

# Input:
# N = 4
# start[] = {1, 3, 2, 5}
# end[] = {2, 4, 3, 6}
# Output: 
# 3




class Solution:
    #Function to find the maximum number of activities that can be performed by a single person.

    def activitySelection(self,n,start,end):
        # Combine the start and end times into a list of tuples
        activities = list(zip(start , end))

        # Sort the activities based on their end times
        activities.sort(key = lambda x : x[1])

        #Initialize
        count = 1 
        prev_end = activities[0][1]

        #start for looop

        for i in range(1 , n):

            if activities[1][0] > prev_end:
                count += 1
                prev_end = activities[i][1]

        return count