# Advent of Code, Day 6, part a
# Lee Cattarin

def string(nums):
    strs = [str(val) for val in nums]
    return "|".join(strs)

f = open("input.txt", "r")
data = f.read()
f.close()

banks = [int(num) for num in data.split()]
seen = set()

while not string(banks) in seen:

    seen.add(string(banks))

    # since index() returns the first item w/ that value, this fulfills
    # need for earlier banks to win in ties
    target = banks.index( max(banks) )
    distribute = banks[target]
    banks[target]=0

    while distribute > 0:
        target += 1
        if target == len(banks):
            target = 0

        banks[target] += 1
        distribute -= 1

print(len(seen))
