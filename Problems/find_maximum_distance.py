# Given an array that might contain duplicate elements, find the maximum possible distance between occurrences of two repeating elements i.e. elements
# having the same value. If there are no duplicate elements in the array, return 0.

# Sample Input :

# 9
# 1  3  1  4  5  6  4  8  3

# Sample Output :

# 7

# Approach - 1
def getMaximumDistance(arr, n):
    d = {}
    for i in range(n):
        d[arr[i]] = d.get(arr[i], 0) + 1
    max_d = 0
    #print(d)
    max_d = 0
    for ele in d:
        if d[ele] > 1:
            first, second, count= -1, -1, 0
            for i in range(n):
                if arr[i] == ele:
                    count += 1
                    if count < 2:
                        first = i
                    else:
                        second = i
            curr_max = second - first
            if curr_max > max_d:
                max_d = curr_max
    return max_d



n = int(input())
arr = [int(x) for x in input().split()]
print(getMaximumDistance(arr, n))


# Approach - 2
# Intuition: We will keep track of the first index of the occurence of every element done at line 50 & at line 53, if the current array element is already present in the 
# dictionary then we will find the difference between it's current index and first index and consider it as the max element
def getMaximumDistance(arr, n):
    d = {}
    max_d = 0
    for i in range(n):
        if arr[i] not in d.keys():
            d[arr[i]] = i
        
        else:
           max_d = max(max_d, i - d[arr[i]])
    return max_d

n = int(input())
arr = [int(x) for x in input().split()]
print(getMaximumDistance(arr, n))

