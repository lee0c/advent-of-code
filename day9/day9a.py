# Advent of Code, Day 9, Part a
# Lee Cattarin

f = open("input.txt")
stream = f.read()

level = 0
score = 0
in_garbage = False
skip_next = False

for char in stream:
    # Last char was !
    if skip_next:
        continue

    if char == "!":
        skip_next = True

    # Garbage handling
    elif in_garbage:
        if char == ">":
            in_garbage = False
    elif char == "<":
        in_garbage = True

    # Groups
    elif char == "{":
        level += 1
    elif char == "}":
        score += level
        level -= 1

print(score)
