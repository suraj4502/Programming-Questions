'''
Problem: Given a string, calculate the sum of numbers in a string (multiple consecutive digits are considered one number)

Examples:

Example 1:
Input: string = “123xyz”
Output: 123

Example 2:
Input: string = “1xyz23”
Output: 24
'''

def number_sum(string):
    answer = 0
    str_chars = []
    for i in string:
        if i.isdigit():
            answer += int(i)
        else:
            str_chars.append(i)
    return answer


if __name__ == "__main__" :
    string = input("Enter the string : ")
    answer = number_sum(string)
    print(answer)
