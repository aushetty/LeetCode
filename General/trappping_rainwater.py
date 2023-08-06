


class Solution:
    def trap(self, height):
        # Current position's amount of water filled = max(left building) - max(right building) - current height
        n = len(height)
        # Storing max on the left side
        leftMax = []
        
        # Storing max on the right side
        rightMax = [0]*n
        

        # Fill up the left max:
        leftMax.append(height[0])

        for i in range(1,n):
            leftMax.append(max(leftMax[i-1],height[i]))


        # Fill up the right max:
        rightMax[n-1] = height[n-1]

        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        
        result = 0
        for i in range(n):
            result += min(leftMax[i],rightMax[i]) - height[i]
            
        return  result