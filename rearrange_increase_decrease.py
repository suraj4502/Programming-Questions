'''
Problem Statement: Rearrange the array such that the first half is arranged in increasing order, 
and the second half is arranged in decreasing order

Examples:

Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
Explanation: First three elements are in the ascending order and next three elements are in the 
descending order.

Example 2:
Input: 4 2 8 6 15 5 9 20
Output: 2 4 5 6 20 15 9 8
'''



def arrange_numbers(array):
    n = len(array)
    half = n//2  # // integer Division 

    array[: half] = sorted(array[: half]) #from starting to half

    array[half:] = sorted(array[half:],reverse=True) #from half to end

    return array


if __name__=='__main__':
    arr = list(map(int,input().split()))
    print(arrange_numbers(arr))
