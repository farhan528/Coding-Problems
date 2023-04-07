# Given a decimal number (integer N), convert it into binary and print.

n = int(input())
arr = []

while(True):
    quotient = n % 2
    arr.append(quotient)
    n = n // 2
    if n==0:
        break

for i in range(len(arr)-1, -1, -1):
    print(arr[i],end="")
