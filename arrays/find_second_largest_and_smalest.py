'''
Problem Statement: Given an array, 
find the second smallest and second largest element in the array. 
Print ‘-1’ in the event that either of them doesn’t exist.

Examples:

Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	    Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and 
hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, 
it is the largest and smallest element present in the array. 
There is no second largest or second smallest element present.
'''

array1 = [1,2,4,7,7,5]

def get_2nd_largest_and_smallest(nums,n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    arr = sorted(nums)
    small = arr[1]
    large = arr[n-2]
    print("Second smallest is", small)
    print("Second largest is", large)



def secondSmallest(arr,n):
    if (n<2):
        return -1
    small = float('inf')
    sSmall = float('inf')

    for i in range(n):
        if (arr[i] < small):
            sSmall = small
            small = arr[i]
        elif (arr[i] != small and arr[i]<sSmall):
            sSmall = arr[i]
            
    return sSmall
            
            
def secondLargest(arr,n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    
    for i in range(n):
        if (arr[i]>large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    
    return second_large
            
            

if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5,1,8,9]
    n = len(arr)
    print(secondSmallest(arr, n))
    print(secondLargest(arr,n))
    