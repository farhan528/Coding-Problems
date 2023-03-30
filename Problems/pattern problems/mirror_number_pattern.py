#    1
#   12
#  123
# 1234


n = int(input())

for i in range(1, n+1):
    count_space = 0
    for spaces in range(n-i):
        print(" ", end="")
        count_space +=1
    count = 1
    for num in range(count_space, n):
        print(count, end="")
        count +=1
    print()        
