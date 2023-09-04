'''
	https://projecteuler.net/problem=1
	MULTIPLES OF 3 OR 5
'''

def problem1(n):
    return sum(i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0))

problem1(1000)

'''
	Answer: 233168
'''
