'''
Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

Note: A palindromic number is a number that remains the same when its digits are reversed.OR  
      a palindrome is a number that reads the same forward and backward Eg: 121,1221, 2552

Examples:

Example 1:
Input: min = 10 , max = 50
Output: 11 22 33 44 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

Example2:
Input: min = 100 , max = 150
Output: 101 111 121 131 141 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.
'''



def All_palindrome_in_given_range(min,max):
    result = []
    for i in range(min,max+1):
        num = str(i)
        if num == num[::-1]:
            result.append(i)
            
    return result
       
print(*(All_palindrome_in_given_range(10,110)))
print(*(All_palindrome_in_given_range(0,220)))
print(*(All_palindrome_in_given_range(10,50)))