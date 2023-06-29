'''
Problem Statement: Write a program to remove all characters from a string except alphabets in a given string.

Examples:

Example 1:
Input: string str = "take12% *&u ^$#forward"
Output: takeuforward
Explanation:
Characters 1,2,%,*,&,^,$,# along with whitespaces are 
removed but the order of remaining alphabets is preserved.

Example 2:
Input: String str = "1.Python & 2.Java"
Output: PythonJava
Explanation: 
Characters 1.&2. along with whitespaces are removed 
but the order of remaining alphabets is preserved.
'''
import re



def remove_special_chars(string):
    pattern = r'[^a-zA-Z0-9\s]'
    result = re.sub(pattern, '',string)
    return result


s = "take12% *&u ^$#forward"
print(remove_special_chars(s))