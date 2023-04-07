# Given a binary number as an integer N, convert it into decimal and print.


n = int(input())
pv, ans = 0, 0

while(n!=0):
    rem = n % 10
    ans += (2 ** pv) * rem
    n = n // 10
    pv +=1

print(ans)
