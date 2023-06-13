
#https://leetcode.com/problems/sort-an-array/



#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

nums = [5,2,3,1]

class Solution:
    def sortArray(self, nums) :
        
        def merge(arr , L , M , R ):
            left , right = arr[L: M+1] , arr[M+1: R+1]
            i, j,k = L , 0 , 0

            while j < len(left) and  k < len(right):
                if left[j] <= right[k]:
                    arr[i] =  left[j]
                    j+= 1
                else:
                    arr[i] = right[k]
                    k+= 1
            
                i+= 1


            while j < len(left):
                nums[i] = left[j]
                j+=1 
                i+=1

            while j < len(right):
                nums[i] = right[k]
                k+=1 
                i+=1

        def mergesort(arr , l, r):
            if l == r:
                return arr
        #creating a recursion  over here
            m = (l + r) // 2
            mergesort(arr, l , m)
            mergesort(arr, m+1, r)
            merge(arr , l , m , r)

            return arr

        return mergesort(nums , 0 , len(nums)- 1))