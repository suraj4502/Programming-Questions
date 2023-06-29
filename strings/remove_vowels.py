'''
Problem Statement: Given a String, write a program to remove vowels from a given String.

Examples:

Example 1:
Input: Str = “take u forward”
Output: tk  frwrd
Explanation: All vowels are removed from the given String.

Example 2:
Input: Str = “I am very happy today”
Output:  m vry happy tdy
Explanation: All vowels are removed from the given String.
'''

s = 'I am very happy today'

s = s.lower()
vowels = ['a','e','i','o','u']
result = []
for i in s:
    if i not in vowels:
        result.append(i)
        
print(*(result))


def remove_vowels(string):
    vowels = ['a','e','i','o','u']
    r1 = [i for i in string.lower() if i not in vowels]
    print("".join(r1))
    
remove_vowels(s)
