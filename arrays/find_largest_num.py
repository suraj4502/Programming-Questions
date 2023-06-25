'''
Problem Statement: Given an array, we have to find the largest element in the array.

Examples:

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
'''

def find_largest_num(nums):
    if nums is None or len(nums) == 0:
        return None
    
    arr = sorted(nums,reverse=True)
    return arr[0]

#2nd approach
def find_largest_num(nums):
    if nums is None or len(nums) == 0:
        return None
    
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest =num
            
    return largest


array1 = [2,5,1,3,0]
array2 = [8,10,5,7,9]

print(find_largest_num(array1))
print(find_largest_num(array2))
