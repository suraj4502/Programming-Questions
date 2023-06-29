'''
Find the ASCII value of a character
Problem Statement: Given a character, Find the ASCII value of the character.

Examples:

Example 1:
Input: c = 'A'
Output: 65
Explanation: ASCII value of A is 65

Example 2:
Input: c = 'e'
Output: 101
Explanation: ASCII value of e is 101
'''


def get_ASCII(letter):
    return ord(letter)

print(get_ASCII('A'))
print(get_ASCII('s'))
print(get_ASCII('e'))