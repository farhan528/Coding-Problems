def get_fib(n):
    if n <= 1:
        return n
    else:
        return (get_fib(n-1) + get_fib(n-2))

limit = int(input("Enter the limit for Fibonacci Sequence: "))
if limit < 0:
    print("Enter a +ve number")
else:
    for i in range(limit):
        print(get_fib(i))
