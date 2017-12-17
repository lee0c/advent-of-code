# Advent of Code, Day 16, Part a
# Lee Cattarin

def swap(li, i1, i2):
    temp = li[i1]
    li[i1] = li[i2]
    li[i2] = temp

f = open("input.txt")
data = f.read().strip().split(",")
f.close()

for i, inst in enumerate(data):
    if inst[0] == "s":
        data[i] = (inst[0], int(inst[1:]))
    elif inst[0] == "x":
        pos = [int(x) for x in inst[1:].split("/")]
        data[i] = (inst[0], pos[0], pos[1])
    elif inst[0] == "p":
        prog = inst[1:].split("/")
        data[i] = (inst[0], prog[0], prog[1])

programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
    "m", "n", "o", "p"]
cycle_len = 0

i = 0
while i < 1000000000:
    if cycle_len > 0 and i + cycle_len < 1000000000:
        i += cycle_len
        continue

    for inst in data:
        if inst[0] == "s":
            # Spin: sX. last X programs move to the front
            programs = programs[-inst[1]:] + programs[:-inst[1]]

        elif inst[0] == "x":
            # Exchange: xY/Z. switch programs at positions Y and Z
            swap(programs, inst[1], inst[2])

        elif inst[0] == "p":
            # Partner: pY/Z. switch positions of programs Y and Z
            swap(programs, programs.index(inst[1]), programs.index(inst[2]))

    i += 1

    for j in range(len(programs) - 1):
        if programs[j] > programs[j + 1]:
            break
        if j == len(programs) - 2:
            cycle_len = i
            print("cycle found, takes", cycle_len, "repetitions")


for prog in programs:
    print(prog, end="")
print()
