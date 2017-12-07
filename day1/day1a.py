# Advent of Code, Day 1, Part a
# Lee Cattarin

f = open("input.txt", "r")

string = f.read().strip()
numbers = [int(num) for num in list(string)]

captcha = 0
last = -1
for num in numbers:
    if num == numbers[last]:
        captcha += num

    last += 1

print(captcha)
