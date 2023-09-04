'''
	Question 20. Factorial digit sum
	Problem Statement: 
	n! means n × (n − 1) × ... × 3 × 2 × 1

	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

	Find the sum of the digits in the number 100!	

'''

import math
print(sum([int(x) for x in str(math.factorial(100))]))

# ALTERNATE APPROACH WITHOUT USING MATH.FACTORIAL
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);

n_factorial_list = res = [int(x) for x in str(factorial(100))]
digit_sum = 0
for i in n_factorial_list:
    digit_sum += i
print(digit_sum)
