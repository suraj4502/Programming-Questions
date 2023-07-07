'''
Calculate Frequency of characters in a String
Problem Statement: Given a string, calculate the frequency of characters in a string.

Examples:

Example 1:
Input: takeuforward
Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
Explanation: Count of every character of string is printed.

Example 2:
Input: articles
Output: a1 c1 e1 i1 l1 r1 s1 t1 
Explanation: Count of every character of string is printed.
'''


def freq_counter(string):
    
    string = string.lower()   

    freq_dict = {}
    for char in string:
        if char in freq_dict:   # MAIN CONCEPT
            freq_dict[char] += 1
        else:
            freq_dict[char] =1
            
    return freq_dict


if __name__ == "__main__": 
    string = input("ENTER THE STRING : ")
    answer = freq_counter(string)
    # print(answer)
    for key, value in sorted(answer.items()):
        print(f'{key}{value}',end= ' ')
        
    
