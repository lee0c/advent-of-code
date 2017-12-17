# Advent of Code, Day 16, Part a
# Lee Cattarin

def swap(li, i1, i2):
    temp = li[i1]
    li[i1] = li[i2]
    li[i2] = temp

f = open("input.txt")
data = f.read().strip().split(",")
f.close()

programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
    "m", "n", "o", "p"]

for inst in data:
    if inst[0] == "s":
        # Spin: sX. last X programs move to the front
        amt = int(inst[1:])
        programs = programs[-amt:] + programs[:-amt]

    elif inst[0] == "x":
        # Exchange: xY/Z. switch programs at positions Y and Z
        pos1, pos2 = inst[1:].split("/")
        swap(programs, int(pos1), int(pos2))

    elif inst[0] == "p":
        # Partner: pY/Z. switch positions of programs Y and Z
        prog1, prog2 = inst[1:].split("/")
        swap(programs, programs.index(prog1), programs.index(prog2))

for prog in programs:
    print(prog, end="")
print()
