# https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1

class Solution:
    def segregate0and1(self, arr):
        n=len(arr)
        left=0
        right=n-1
        
        while left<right:
            
            if arr[left]==0 and arr[right]==1:
                left+=1
                right-=1
            
            elif arr[left]==1 and arr[right]==0:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
                
            elif arr[left]==0 and arr[right]==0:
                left+=1
                
            elif arr[left]==1 and arr[right]==1:
                right-=1        