'''
Problem Statement: Given a string, write a program to count the number of vowels, consonants, and spaces in that string.

Examples:

Example 1:
Input: string str=”Take u forward is Awesome”
Output: 
Vowels: 10
Consonants: 11
White spaces: 4

Example 2:
Input: string str=”India won the cricket match”
Output:
Vowels: 8
Consonants: 15
White spaces: 4
'''



def counter(string):
    string = string.lower()

    vowels = ['a','e','i','o','u']
    space = ' '

    v_count = 0
    c_count = 0
    s_count = 0
    for i in string:
        if i in vowels:
            v_count +=1
        elif i == space:
            s_count +=1
        else:
            c_count +=1
        
    print("Vowels:",v_count)
    print("Consonants:",c_count)
    print("White spaces:",s_count)


    
string = 'India won the cricket match'
counter(string)