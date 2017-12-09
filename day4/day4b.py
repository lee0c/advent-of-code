# Advent of Code, Day 4, Part b
# Lee Cattarin

valid_passphrases = 0

for line in open("input.txt", "r"):
    terms = ["".join(sorted(term)) for term in line.split()]
    termset = set(terms)
    if len(terms) == len(termset):
        valid_passphrases += 1

print(valid_passphrases)
