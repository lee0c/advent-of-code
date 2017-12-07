# Advent of Code, Day 1, Part b
# Lee Cattarin

f = open("input.txt", "r")

string = f.read().strip()
string = "1212"
numbers = [int(num) for num in list(string)]

captcha = 0
last = len(numbers)//2
for num in numbers:
    if num == numbers[last]:
        captcha += num

    last += 1
    if last == len(numbers):
        last = 0

print(captcha)
