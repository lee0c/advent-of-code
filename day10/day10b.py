# Advent of Code, Day 10, Part b
# Lee Cattarin

from functools import reduce

f = open("input.txt", "r")
lengths = f.read().strip()
f.close()

lengths = [ord(x) for x in lengths] + [17, 31, 73, 47, 23]

ring = [x for x in range(256)]
pos = 0
skip = 0

# sparse hash
for i in range(64):
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

#dense
dense = ""
xorred = []
for i in range(16):
    xorred.append( reduce( (lambda x, y: x^y), ring[i*16:i*16+16]) )

dense = ["{:02x}".format(x) for x in xorred]
dense = "".join(dense)

print(dense)
