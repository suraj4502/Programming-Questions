'''
Problem Statement: You are given an array. The task is to reverse the array and print it. 

Examples:

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth 
position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth
position, the second element occupies the fourth position and so on.
'''

def reverse_array(arr):
    # Initialize start and end pointers
    start = 0
    end = len(arr) - 1
    
    # Swap elements from start to end until they meet in the middle
    while start < end:
        # Swap elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]
        # Move start pointer forward
        start += 1
        # Move end pointer backward
        end -= 1
    
    return arr


# def reverse_array(arr):
#     start = 0
    
#     end = len(arr)-1
    
#     while start < end :
#         arr[start] , arr[end] = arr[end] , arr[start]
        
#         start +=1
#         end -=1
        
        

#     return arr

def reverse_array(arr):
    return arr[::-1]

# Test the code with examples
arr1 = [5, 4, 3, 2, 1]
print(reverse_array(arr1))  # Output: [1, 2, 3, 4, 5]

arr2 = [10, 20, 30, 40]
print(reverse_array(arr2))  # Output: [40, 30, 20, 10]
