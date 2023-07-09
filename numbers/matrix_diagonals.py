'''
Given a Square Matrix, calculate the absolute
difference between the sums of its diagonals.
123
456
987
'''

# mat = [[1,2,3],[4,5,6],[9,8,7]]

# ltr= 0   #left TO right
# rtl = 0  #Right TO left
# # print(len(mat))

# for i in range(len(mat)):
#   for j in range(len(mat)):
#     if i == j:
#       ltr += mat[i][j]
      
#     elif i+j == (len(mat) -1):
#       rtl += mat[i][j]
# print(ltr)
# print(rtl)
# print("Result : ", ltr - rtl)



def digonal_diff(matrix):
  l_to_r = 0
  r_to_l = 0

  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if i ==j :
        l_to_r += matrix[i][j]
      elif i +j == (len(matrix)-1):
        r_to_l += matrix[i][j]

  return (l_to_r - r_to_l)


mat = [[1,2,3],
       [4,6,6],
       [9,8,7]]
print("Result : ", digonal_diff(mat))
  