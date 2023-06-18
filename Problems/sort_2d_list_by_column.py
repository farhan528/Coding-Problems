# Problem Statemnt:
# Sort a given 2D array of shape (4, 5) by 2nd column (i.e. column at index 1) in ascending order.
# That means, we should re-arrange complete row based on 2nd columns' values.
# Given 2D array is:

#  [[21 20 19 18 17]
#   [16 15 14 13 12]
#   [11 10  9  8  7]
#   [ 6  5  4  3  2]]

# Print the 2D array in sorted order.
# Note you have to generate the 2D Array.Here 2nd column means column present at index 1.
# Output Format :

# [[ 6  5  4  3  2]
# [11 10  9  8  7]
# [16 15 14 13 12]
# [21 20 19 18 17]]


# Approach - 1
import numpy as np

a =  np.array([[21, 20, 19, 18, 17],
              [16, 15, 14, 13, 12],
              [11, 10,  9,  8,  7],
              [6,  5 , 4 , 3 , 2]])

b = a[:,1].copy()
b.sort()

for i in range(len(a)):
    row2 = np.where(a[:,1]==(b[i]))
    temp = a[i].copy()
    a[i] = a[row2]
    a[row2] = temp
print(a)




# Approach - 2
import numpy as np

a = np.arange(21,1,-1)
a = a.reshape(4,5)
a = a[a[:,1].argsort()]
print(a)
