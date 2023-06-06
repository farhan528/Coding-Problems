# You are provided with an integer array where each number is present either odd number of times or even number of times. You have to find and return the number which is present even number of times.
# If multiple numbers are present even number of times, then return that number which occurs first among these numbers in the given array. If no such number exists, then return -1.

# Sample Input:
# 6
# 2 5 3 5 3 4 
# Sample Output:
# 5

def evenCount(arr, n):
    d = {}
    for i in range(n):
        d[arr[i]] = d.get(arr[i], 0) + 1
    for ele in arr:
        if d[ele] % 2 == 0:
            return ele

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(evenCount(arr, n))

