import numpy as np

np1 = np.arange(10)

print(np1)
print(np1[2:8]) # from 2 to 8 but eight is excluded
print(np1[2:8:3]) # from2 to 8 in step of 3
print(np1[::2]) # in step of 2
print(np1[::3]) # in step of 3

#Slice a 2d array

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np2[1,2]) # slice single number

# slice a 2d array 2,3

print(np2[0:1,1:3])