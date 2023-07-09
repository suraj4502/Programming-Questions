'''
Question 2:
Given a array of integers with size 'num' and another number
'num2'. Also given a size 'S' (Integer Value) of the Subset. The
task is to find if the number 'num2' is present in every non-
overlapping subset of size 'S' in the given array. Return '1' if true,
else return 'O'.
For Example:
Input-
12
20 1 6 8 13 20 1 7 20 13 16 20
20
3

Output-
1
'''

def num_in_subarray(n,arr,num,sub_len):
  # Iterate over the array in steps of size sub_len
  for i in range(0,n,sub_len):
    # Create a subset by slicing the arr array from the current index i to the i + sub_len-th element (not inclusive)
    subset = arr[i:i+sub_len]
    # Check if the num value is present in the current subset
    if num not in subset:
      # If the value is not found, return 0
      return 0
  # If the loop completes without returning early, it means that the num value was found in all of the subsets
    # In this case, return 1 to indicate that the number is present in every subset  
  return 1



n = 12
arr = [20, 1, 6, 8, 13, 20, 1, 7, 20, 13, 16, 20]
num = 20
sub_len = 3

print(num_in_subarray(n,arr,num,sub_len))

# ------------------------------------------------------------

def in_subarray(n,arr,num,s):
  for i in range(0,n,s):
    subset = arr[i:i+s]
    if num not in subset:
      return 0
      
  return 1


n = 12
arr = [20, 1, 6, 8, 13, 20, 1, 7, 2, 13, 16, 20]
num = 20
sub_len = 3

print(in_subarray(n,arr,num,sub_len))




# if __name__ == "__main__":
#   n = int(input())
#   arr = list(map(int,input().split()))
#   num = int(input())
#   sub_len = int(input())

#   print(num_in_subarray(n,arr,num,sub_len))
  
