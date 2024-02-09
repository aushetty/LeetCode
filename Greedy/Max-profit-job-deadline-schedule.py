#https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1


# Driver code is a mess need to take care


# Example-1
# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).

# Example-2
# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).






#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        ## Sort jobs based on their profits in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        

        #count of number of deadline output given here is max deadline entity in the job object 
        max_deadline = max(Jobs, key=lambda x: x.deadline).deadline


        time_slots = [0] * max_deadline  # Array to keep track of available time slots
        
        total_profit = 0
        jobs_done = 0
        
        for job in Jobs:
            # Find a time slot before or at the deadline
            for i in range(job.deadline - 1, -1, -1):
                if time_slots[i] == 0:
                    time_slots[i] = job.id
                    total_profit += job.profit
                    jobs_done += 1
                    break
                    
        return jobs_done, total_profit
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends