import numpy as np

##########################################################
# NUMPY ARRAYS VS. PYTHON LISTS
##########################################################

# creating numpy array from list

nlist = [1, 2, 3, 4, 5, 6]
nparray = np.array(nlist)
print(nparray)

# printing is the same

for i in nlist:
    print(i)

for i in nparray:
    print(i)

# + signals causes different effects // concatenation vs. vector addition

nlist = nlist + [7] # for lists results in concatenation
nlist.append(8)
for i in nlist:
    print(i)

nparray = nparray + [7] # for numpy arrays results in addition to all indexes
for i in nparray:
    print(i)

# numpy arrays simplify adding arrays

nparray2 = nparray + nparray
for i in nparray2:
    print(i)
print("\n")

nlist2 = nlist + nlist # concatenation in lists
for i in nlist2:
    print(i)
print("\n")

nlist3 = []
for i in nlist:
    nlist3.append(i + i) # vector addition in lists
for i in nlist3:
    print(i)
print("\n")

# scalar multiplication vs. vector multiplication

nlist4 = [1, 2, 3]
nparray3 = np.array(nlist4)

nlist4 = nlist4 * 2
print(nlist4)
print("\n")

nparray3 = nparray3 * 2
print(nparray3)
print("\n")

# power, square, log and exp

nparray3 = nparray3**2 # power operation // this would require a loop for lists
print(nparray3)
print("\n")

nparray3 = np.sqrt(nparray3)
print(nparray3)
print("\n")

nparray3 = np.log(nparray3)
print(nparray3)
print("\n")

nparray3 = np.exp(nparray3)
print(nparray3)
print("\n")

# loops are slower than numpy arrays