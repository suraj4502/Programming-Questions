'''
Given a string, check if the string is palindrome or not.”  A string is said to be palindrome if the reverse of the string is the same as the string.

Examples:

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
'''

def is_palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    s = input("Enter the String to check : ")
    if is_palindrome(s):
        print("Palindrome")
    else:
        print("Not Palindrome")
