'''
Problem Statement:  Given a number check if it is a palindrome.

An integer is considered a palindrome when it reads the same backward as forward.

Examples:

Example 1:
Input: N = 123
Output: c
Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

Example 2:
Input: N =  121 
Output: Palindrome Number
Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.
'''

nums = input("Enter the number:" )

nums = str(nums)

nums_r = nums[::-1]

if nums == nums_r:
    print('Palindrome Number') 
else:
    print('Not Palindrome Number')