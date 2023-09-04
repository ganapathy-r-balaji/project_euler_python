'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
Find the product abc.


'''

for i in range(1,1000):
    for j in range(i+1,1000):
        k = 1000 - i - j
        if i ** 2 + j ** 2 == k ** 2: break
    if i**2 + j**2 == k**2: break

print(i*j*k)
