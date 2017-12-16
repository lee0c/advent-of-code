# Advent of Code, Day 13, Part a
# Lee Cattarin

depth = []

for line in open("input.txt"):
    data = line.strip().split(": ")
    while int(data[0]) > len(depth):
        depth.append(0)
    depth.append(int(data[1]))

step = 0
severity = 0

while step < len(depth):
    if depth[step] != 0 and step % ( (depth[step] - 1) * 2 ) == 0:
        severity += step * depth[step]
    step += 1

print(severity)
