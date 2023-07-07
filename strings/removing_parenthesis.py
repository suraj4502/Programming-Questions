'''
Remove brackets from an algebraic expression

Write a program to remove brackets from an algebraic expression

Given an algebraic expression, we need to simplify the expression and remove the brackets.

Examples:

Example 1:
Input: “a+((b-c)+d)”
Output: “a+b-c+d”
Explanation: Removed all the brackets in the algebric expression.

Example 2:
Input: “(((a-b))+c)”
Output: “a-b+c”
Explanation: Removed all the brackets in the algebric expression.
'''


def remove_parenthesis(string):
    answer = []
    for i in string:
        if i != "(" and i != ")":
            answer.append(i)
    return answer
     
     
if __name__ == "__main__"  :
    s = 'a+((b-c)+d)' 
    answer = remove_parenthesis(s)
    print("".join(answer))