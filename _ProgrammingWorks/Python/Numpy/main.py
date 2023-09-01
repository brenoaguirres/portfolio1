import numpy as np

##########################################################
# CREATING SPECIFIC ARRAYS, RESHAPE AND MORE
##########################################################

# array of zeroes
zero_array = np.zeros((2, 3))
print(zero_array)

# array of ones
ones_array = np.ones((2, 3))
print(ones_array)

# initialize data type
ones_array = np.ones((3, 2), dtype=np.int16)
print(type(ones_array[0, 0]))

# empty array
empty_array = np.empty([3, 3], dtype=np.int16)
print(empty_array)

# create array within a range --- max exclusive
range_array = np.arange(1, 5)
print(range_array)

range_array = np.arange(1, 5, .5) # the step / interval
print(range_array)

# create array of evenly spaced values within a range
print(np.linspace(1, 5))

print(np.linspace(1, 5, 5)) # specifies number of elements

# array of random numbers
print(np.random.random((2, 3)))

# RESHAPING ARRAYS
ar = np.zeros((2, 3))
print(ar)
ar.reshape((6, 1)) # new dimensions needs to conform to the original dimensions
print(ar)