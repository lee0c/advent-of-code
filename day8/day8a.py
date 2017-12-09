# Advent of Code, Day 8, Part a
# Lee Cattarin

def compare(var, cond, val):
    if registers[var] == val:
        if cond in ["==", ">=", "<="]:
            return True
        else:
            return False

    if registers[var] > val and cond in [">", ">="]:
        return True
    if registers[var] < val and cond in ["<", "<="]:
        return True
    if cond == "!=":
        return True

    return False

registers = {}
top = 0

for line in open("input.txt", "r"):
    inst = line.strip().split()

    reg = inst[0]
    op = inst[1]
    amt = int(inst[2])
    # inst[3] is if, always
    var = inst[4]
    cond = inst[5]
    val = int(inst[6])

    # add registers if needed
    if reg not in registers:
        registers[reg] = 0
    if var not in registers:
        registers[var] = 0

    # check the conditional section
    if compare(var, cond, val):
        if op == "inc":
            registers[reg] += amt
        elif op == "dec":
            registers[reg] -= amt

    if registers[reg] > top:
        top = registers[reg]

print(top)
