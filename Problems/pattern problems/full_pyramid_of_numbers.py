#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5



n = int(input())
limit = 1
for i in range(1,n+1):
    count_space = 0
    for spaces in range(n-i):
        print(" ", end="")
        count_space +=1
    flag = True
    left = i
    subtract = 2
    for j in range(count_space, n+i-1):
        if left > limit:
            flag = False
            right = left - subtract
        if flag:
            print(left, end="")
            left += 1
        else:
            print(right, end="")
            subtract += 1
    limit += 2
    print()

        
