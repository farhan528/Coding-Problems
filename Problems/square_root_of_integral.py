# Given a number N, find its square root. You need to find and print only the integral part of square root of N.
# For eg. if number given is 18, answer is 4.


n = int(input())
mul = 1
count = 0
while True:
    num = mul * mul
    if num <= n:
        count += 1
        mul += 1
    if num > n:
        break
print(count)
