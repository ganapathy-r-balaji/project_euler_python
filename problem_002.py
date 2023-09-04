'''
Even Fibonacci Numbers
Problem 2
https://projecteuler.net/problem=2
'''

def fibonacci_generator(i):
    m, n = 1, 1
    while n <= i:
        m, n = n, m+n
        yield m
    
def problem2(n):
    return sum(i for i in fibonacci_generator(n) if not i%2)

problem2(4000000)

'''
	Answer: 4613732
'''
