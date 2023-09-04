'''
Summation of primes
Problem 10
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Answer: 142913828922

'''

import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % j for j in range(3, int(math.sqrt(n)) + 1, 2))


results = 0
for i in range(2, 2000001):
    if is_prime(i):
        results += i
print(results)
