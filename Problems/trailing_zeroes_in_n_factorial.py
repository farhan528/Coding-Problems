# Find and return number of trailing 0s in n factorial without calculating n factorial.

# Intuition:
#   For any given number n, the no of trailing zeroes in n! would be dependent upon the number of 10s or 2s x 5s are there. And for any positive integer it is a general
#   obervation that the primt factor of any number will have occurences of 2s > 5s. So, basically we will calculate only the occurences of 5s because those many 5s will
#   be paired with 2s to form 10. To calculate number of 5s in any given number we can use legendre's formula in which we keep on dividing n by 5 ** k, where 1<=k and
#   k goes until 5 // 5**k isn't 0


n = int(input())
power, trailing_zeroes = 1, 0
while True:
    current_power = n // (pow(5,power))
    if current_power == 0:
        break
    trailing_zeroes += current_power
    power += 1

print(trailing_zeroes)
