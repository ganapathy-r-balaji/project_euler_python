'''
Lattice paths
Problem 15
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, here are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

Answer: 137846528820
'''

def lattice_paths(n):
    line = [1]
    lines = 0
    while lines < n:
        i = 0
        newline = [1, 1]
        while len(newline) - 1 <= lines and len(line) - 1 > i:
            new = line[i] + line[i + 1]
            newline.insert(i + 1, new)
            i += 1
        line = newline
        lines += 1

    return line


pascal_line = lattice_paths(40)
middle = len(pascal_line) // 2
print(pascal_line[middle])
