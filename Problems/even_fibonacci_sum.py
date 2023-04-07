# Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N.
# Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.
# Sample Input 1:
# 8
# Sample Output 1 :
# 10
# Sample Input 2:
# 400
# Sample Output 2:
# 188

n = int(input())
ans = 0

def getFib(n):
    if n <=1 :
        return n
    return getFib(n-1) + getFib(n-2)

for i in range(1, n+1):
    current_fib = getFib(i)
    if current_fib >= n:
        break
    if current_fib % 2 == 0:
        ans += current_fib
print(ans)
