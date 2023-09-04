'''
Longest Collatz sequence
Problem 14
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:
								n → n/2 (n is even)
								n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
					13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
It is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

def longest_collatz_sequence(n):
    terms = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        terms += 1
    return terms

most = 0
i = 1
while i < 10 ** 6:
    s = longest_collatz_sequence(i)
    if s > most:
        most = s
        value = i
    i += 1
print(value)
