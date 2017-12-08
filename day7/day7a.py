# Advent of Code, Day 7, Part a
# Lee Cattarin

from Node import Node

programs = {}

for line in open("input.txt", "r"):
    # print(line)

    data = line.strip().split()

    # first node in chain
    name = data[0]
    weight = int(data[1][1:-1])

    if name in programs:
        programs[name].weight = weight
        # print("Updated primary node:", programs[name])

    else:
        programs[name] = Node(name, weight)
        # print("Added primary node:", programs[name])

    if len(data) > 2:
        # this has children
        children = [child.replace(",","") for child in data[3:]]

        for child in children:

            if not child in programs:
                programs[child] = Node(child)
                # print("Added child node:", programs[child])

            programs[child].parent = name
            # print("Updated child node:", programs[child])

while not programs[name].parent == None:
    name = programs[name].parent

print(name)
