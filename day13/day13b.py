# Advent of Code, Day 13, Part b
# Lee Cattarin

depth = []

for line in open("input.txt"):
    data = line.strip().split(": ")
    while int(data[0]) > len(depth):
        depth.append(0)
    depth.append(int(data[1]))

step = 0
delay = 0

while step < len(depth):
    if depth[step] != 0 and (step + delay) % ( (depth[step] - 1) * 2 ) == 0:
        delay += 1
        step = 0
        continue
    step += 1

print(delay)
