# Advent of Code, Day 2, Part a
# Lee Cattarin

f = open("input.txt", "r")

checksum = 0

for line in f:
    row = [int(num) for num in line.strip().split("\t")]

    checksum += max(row) - min(row)

print(checksum)
