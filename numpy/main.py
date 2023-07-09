import numpy as np

# One dimensional array can be created using ‘arange
a = np.arange(1,10)  # last element i.e. 10 is not included in result
print(a,a.shape)

b = np.arange(1,20,2) # print 1 to 10 with the spacing of 2
print(a,a.shape)

c = np.arange(40,2,-3) # last element 2 is not included in result self
print(c,c.shape)

print("------------------------------")
#  ARRAYS

a= np.array([1, 8, 2])
print(a) # [1 8 2]
print(np.shape(a)) # (3,)

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(b)
print(b.shape)

c=np.array([[np.arange(1,10)],[np.arange(11, 20)]])
print(c)
print(c.shape)

print("------------------------------")
#Matrix

a = np.mat('1,2;3,4;5,6')
print(a)
print(a.shape)
print(type(a))

print("--")

arr = np.array([[1,2,3],[4,5,6]])
mat = np.mat(arr)
print("matrix : %s" %mat)

transpose = np.transpose(mat)
print("Transpose of matrix : %s" %transpose)

print("--")

# eye(n) is used for (nxn) Identity matrix
b=2*np.eye(3) # 2 * Identity matrix
print(b)
print(np.shape(b)) # (3, 3)

c = np.eye(4)
print(c)
print(np.shape(c))

d = 3* np.eye(3)
print("Matrix Multiplication : ")
print(b*d)

