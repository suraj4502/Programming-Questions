'''
Problem Statement: Given an array, we have to find the smallest element in the array.

Examples:

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 0
Explanation: 0 is the smallest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 5
Explanation: 5 is the smallest element in the array.
'''



def find_smallest_num(nums):
    if nums is None or len(nums) == 0:
        return None
    
    arr = sorted(nums)
    return arr[0]


# another Approach

def find_smalles_num(nums):
    if nums is None or len(nums) == 0:
        return None
    
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        
    return smallest
 
array1 = [2,5,1,3,0]  
array2 = [8,10,5,7,9] 
print(find_smallest_num(array1))
print(find_smallest_num(array2))
