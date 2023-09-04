'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

Answer: 104743
'''
def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break

        else:
            prime_list.append(num)

        num += 2

    return prime_list[-1]  

n = 10001
nth_prime_number(n)
