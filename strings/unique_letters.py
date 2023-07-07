'''
Problem:  Given a string, print non-repeating characters of the string.

Examples:

Example 1:
Input: string = “google”
Output: l,e

Explanation: Non repeating characters are l,e.

Example 2:
Input: string = “yahoo”
Output: y,a,h
Explanation: Non repeating characters are y,a,h
'''



def get_unique(string):
    string = string.lower()
    freq_dict={}

    for letter in string:
        if letter in freq_dict:
            freq_dict[letter] +=1
        else:
            freq_dict[letter] =1
            
    result = [key for key,value in freq_dict.items() if value == 1]
    return result
    
    
if __name__ == "__main__":
    string = 'surajkumarsfYadav'
    result = get_unique(string)
    print(*(result))
    print(", ".join(result))
    