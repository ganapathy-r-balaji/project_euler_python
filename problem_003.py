'''
Largest Prime Factor
Problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857
'''

def largest_prime_factor(n):
    for i in range(2, n):
        isPrime = True
        if i % 2 == 0 and i != 2:
            continue
        for j in range(2, int(i ** 1 / 2)):
            if j % 2 == 0:
                continue
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            yield i
            
n = 600851475143

for i in largest_prime_factor(n):
    if n % i == 0:
        n /= i
    if n <= 1:
        print(i)
        break
