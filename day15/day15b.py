# Advent of Code, Day 15, Part b
# Lee Cattarin

a = 883
b = 879

a_factor = 16807
b_factor = 48271

limit = 2147483647

matches = 0

for i in range(5000000):
    a = (a * a_factor) % limit
    while a % 4 != 0:
        a = (a * a_factor) % limit

    b = (b * b_factor) % limit        
    while b % 8 != 0:
        b = (b * b_factor) % limit

    a_bin = format(a, "032b")
    b_bin = format(b, "032b")

    for j in range(-1,-17,-1):
        if not a_bin[j] == b_bin[j]:
            break
        if j == -16:
            matches += 1

print(matches)
