'''
Problem Statement: Given a string, write a program to remove all the whitespaces from the string.

Examples:

Example 1:
Input: str = “Take you forward” 
Output: Takeyouforward
Explanation: After removing all the whitespaces Takeyouforward is the result

Example 2:
Input: str = “How are you doing”
Output: Howareyoudoing
Explanation: After removing all the whitespaces Howareyoudoing is the result
'''


def remove_spaces(string):
    return string.replace(" ", "")


print(remove_spaces("SURAJ IS NIGHTWING"))
print(remove_spaces("How are you doing"))
