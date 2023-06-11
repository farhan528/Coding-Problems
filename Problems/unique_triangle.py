# You are given n triangles. You are required to find how many triangles are unique out of given triangles. For each triangle you are given three integers a, b and c (the sides of a triangle).
# A triangle is said to be unique if there is no other triangle with same set of sides.
# In other words, we have to find frequency of each triangle and return the count of triangles whose frequency is 1.
# Note : It is always possible to form triangle with given sides.

# Sample Input :
# 5
# 7 6 5
# 5 7 6
# 8 2 9
# 2 3 4
# 2 4 3

# Sample Output :
# 1

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
m = {}
for i in range(n):
    arr = [int(x) for x in input().split()]
    arr.sort()
    toAdd = ''.join([str(ele) for ele in arr])
    m[toAdd] = m.get(toAdd, 0) + 1
count = 0
for ele in m:
    if m[ele] == 1:
        count += 1
print(count)

