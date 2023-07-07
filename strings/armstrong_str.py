'''
Check if two Strings are anagrams of each other
Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

Examples:

Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.
'''


def str_armstrong(s1,s2):
    s1 = sorted(s1.strip().lower())
    s2 = sorted(s2.strip().lower())

    if s1 == s2 :
        return True
    else:
        return False
    
if __name__ == "__main__":
    s1,s2 = input("ENTER THE STRINGS separated by comma: ").split(',')
    print(f'First string : {s1}')
    print(f'Second String : {s2}')
    print(str_armstrong(s1,s2))