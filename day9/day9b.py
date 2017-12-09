# Advent of Code, Day 9, Part b
# Lee Cattarin

f = open("input.txt")
stream = f.read()

garbage = 0
in_garbage = False
skip_next = False

for char in stream:
    # Last char was !
    if skip_next:
        skip_next = False
        continue

    if char == "!":
        skip_next = True

    # Garbage handling
    elif in_garbage:
        if char == ">":
            in_garbage = False
        else:
            garbage += 1

    elif char == "<":
        in_garbage = True

print(garbage)
