# Advent of Code, Day 10, Part a
# Lee Cattarin

ring = [x for x in range(256)]
pos = 0
skip = 0

f = open("input.txt", "r")
lengths = f.read().strip()
lengths = [int(x) for x in lengths]

for length in lengths:
    if length + pos >= len(ring):
        section = ring[pos:] + ring[:length - (len(ring) - pos)]
    else:
        section = ring[pos:pos + length]
    section = section[::-1]

    for val in section:
        ring[pos] = val
        pos += 1
        if pos == len(ring):
            pos = 0

    pos += skip
    pos = pos % len(ring)
    skip += 1

print(ring[0] * ring[1])
