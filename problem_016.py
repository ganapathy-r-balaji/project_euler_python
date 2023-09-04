'''
Power Digit Sum
Problem 16
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
What is the sum of the digits of the number 2^1000?

Answer: 1366
'''

# Approach 1:
n = pow(2, 1000)
val = 0
while(n > 0):
    val += n%10
    n = n//10
print(val)

# Approach 2:
print(sum(map(int, str(2**1000))))
