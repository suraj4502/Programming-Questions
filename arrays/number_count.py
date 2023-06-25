'''
Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Examples:

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
        15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	3  1
        4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array
'''


def number_of_occurance(array):
    # Initialize a dictionary to store the count of each number
    count = {}

    # Loop through each number in the array
    for num in array:
        # If the number is already in the dictionary, increment its count
        if num in count:
            count[num] += 1
        # Otherwise, add the number to the dictionary with a count of 1
        else:
            count[num] = 1

    # Sort the dictionary by value (count) in descending order
    sorted_dict = dict(sorted(count.items(), key=lambda x: -x[1]))

    # Return the sorted dictionary
    return sorted_dict



# Check if the script is being run as the main program
if __name__ == '__main__':
    # Read in the input array from the user as a string, split it into a list of integers, and convert it to a list
    arr = list(map(int, input().split()))

    # Call the number_of_occurance function with the input array as an argument
    result = number_of_occurance(arr)

    # Loop through the sorted dictionary and print out each key-value pair
    for key, value in result.items():
        print(key, value)