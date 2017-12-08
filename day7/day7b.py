# Advent of Code, Day 7, Part a
# Lee Cattarin

from Node import Node

def one_unequal(vals):
    if vals.count(vals[0]) == len(vals):
        return None

    for val in vals:
        if vals.count(val) < len(vals) - 1:
            return vals.index(val)


def dfs_balance(name):
    if programs[name].children == None:
        return programs[name].weight, False

    weights = []
    for child in programs[name].children:
        weight,found = dfs_balance(child)

        # If a node below this has already found the answer
        if found:
            return weight,found

        # Otherwise
        weights.append(weight)

    index = one_unequal(weights)

    if not index == None:
        bad = programs[name].children[index]

        # get the difference in weight
        if weights[index] == weights[0]:
            diff = weights[index] - weights[1]
        else:
            diff = weights[index] - weights[0]

        return programs[bad].weight - diff, True

    return sum(weights) + programs[name].weight, False

programs = {}

for line in open("input.txt", "r"):

    data = line.strip().split()
    name = data[0]
    weight = int(data[1][1:-1])

    if name in programs:
        programs[name].weight = weight
    else:
        programs[name] = Node(name, weight)

    if len(data) > 2:
        # this has children
        children = [child.replace(",","") for child in data[3:]]
        programs[name].children = children

        for child in children:

            if not child in programs:
                programs[child] = Node(child)
            programs[child].parent = name

while not programs[name].parent == None:
    name = programs[name].parent

print(name)

print(dfs_balance(name))
