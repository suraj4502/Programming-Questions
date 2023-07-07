'''
Problem Statement: Given a string, write a program to Capitalize the first and last character of each word of that string.

Examples:

Example 1:
Input: String str = "take u forward is awesome"
Output: “TakE U ForwarD IS AwesomE”
Explanation: We get the result after capitalizing the first and last character of each word of a string

Example 2:
Input: String str = "Take u Forward is Awesome"
Output: “TakE U ForwarD IS AwesomE”
Explanation: Characters T, F, A are initially in uppercase , so they remain as they are in the result.
'''



def Capitalize(string):
    words = string.split()
    answer = []
    for word in words:
        if len(word) >1:
            word = word[0].upper() + word[1:-1] + word[-1].upper()   # MAIN CONCEPT
        else:
            word = word.upper()
        answer.append(word)
    return " ".join(answer)


if __name__ == "__main__":     
    string = input("ENTER THE STRING : ")
    print(Capitalize(string))