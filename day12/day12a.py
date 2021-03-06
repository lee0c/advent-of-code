# Advent of Code, Day 12, Part a
# Lee Cattarin

from Node import Node

programs = {}

for line in open("input.txt"):
    data = line.strip().split(" <-> ")
    name = data[0]
    pipes = data[1].split(", ")

    if name not in programs:
        programs[name] = Node(name)
    programs[name].add_pipes(pipes)

    for pipe in pipes:

        if pipe not in programs:
            programs[pipe] = Node(pipe)
        programs[pipe].add_pipe(name)

connected = set()
tosearch = set()

tosearch.add("0")

while len(tosearch) > 0:
    new = tosearch.pop()
    tosearch = tosearch | programs[new].pipes
    tosearch = tosearch - connected
    connected.add(new)

print(len(connected))
