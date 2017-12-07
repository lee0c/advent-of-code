# Advent of Code, Day 2, Part b
# Lee Cattarin

f = open("input.txt", "r")

checksum = 0

for line in f:
    row = [int(num) for num in line.strip().split("\t")]

    for num1 in row:
        for num2 in row:
            if num1 == num2:
                continue
            if not num1 % num2 == 0:
                continue

            checksum += num1 // num2

print(checksum)
