import numpy as np

##########################################################
# BASIC PROPERTIES AND METHODS IN NUMPY ARRAYS
##########################################################

# arrays and matrixes
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4], [5, 6]])

# index starts at 0
print(a[0])
print(b[0])
print(b[0][0])

# matrix is less recommended on docs
m = np.matrix([[1, 2], [3, 4], [5, 6]])
print(m)

# same result as line 12 notation
print(b[0, 0])

# transpose matrix
print(b.T)

# number of rows and columns // shape
print(b.shape)

c = b.T
print(c.shape)

# number of dimensions
print(b.ndim)

# number of elements
print(b.size)

# type of data
print(b.dtype)

d = np.array([1.1, 1.2])
print(d.dtype)

# converting data type with parameter
e = np.array([1, 2], dtype=np.float64)
print(e)
print(e.dtype)

# memory size of elements
print(b.itemsize)
print(str(b.itemsize) + " bytes")
print(e.itemsize)

# minimum and maximum value on the array
print(b.min())
print(b.max())

# sum elements
print(b)
print(b.sum())
print(b.sum(axis=0)) # sum of the columns
print(b.sum(axis=1)) # sum of the lines