# Advent of Code, Day 11, Part b
# Lee Cattarin

def add_to_path(path, direction, dirs):
    index = dirs.index(direction)
    if dirs[index - 3] in path:
        path.remove(dirs[index - 3])

    elif dirs[index - 2] in path:
        path.remove(dirs[index - 2])
        add_to_path(path, dirs[index - 1], dirs)

    elif dirs[ (index + 2) % 6 ] in path:
        path.remove(dirs[ (index + 2) % 6 ])
        add_to_path(path, dirs[ (index + 1) % 6 ], dirs)

    else:
        path.append(direction)

f = open("input.txt", "r")
path = f.read().strip().split(",")
f.close()

dirs = ["nw", "n", "ne", "se", "s", "sw"]

maxx = 0

newpath = []

for i in range(len(path)):
    add_to_path(newpath, path[i], dirs)

    maxx = max(maxx, len(newpath))

print(maxx)
