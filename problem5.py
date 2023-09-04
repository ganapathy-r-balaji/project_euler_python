'''
Smallest multiple
Problem 5
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

In this problem, I have tried three approaches to implement the logic to this probelm.
Runtime: 
	Solution 1 runtime: 26.377 seconds
 	Solution 2 runtime: 0.0795 seconds
	Solution 3 runtime: 0.0 seconds

Answer: 232792560
'''

# Approach1: brute-force approach
def problem5_approach1():
    divisors = [x for x in range(1, 21)]
    x = 1
    while True:
        smallest = True
        for i in divisors:
            if x % i != 0:
                smallest = False
                break
        if smallest:
            print(x)
            break
        x += 1

# Approach2:
def problem5_approach2(num):
    return all([num%x==0 for x in range(20, 10, -1)])

num = 2520
while True:
    if problem5_soln3(num):
        print(num)
        break
    num+=2520

# Approach3:
def problem5_approach3():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i * j) % k == 0:
                    i *= j
                    break
    print(i)
