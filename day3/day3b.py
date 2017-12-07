# Advent of Code, Day 3, Part b
# Lee Cattarin

import math

def addto(vals, key, inc):
    if not key in vals:
        vals[key] = 0
    vals[key] += inc

src = 265149

vals = {}
# because one is a shitty corner case
for i in range(2,10):
    vals[i] = 1

current = 2
shadow = 11 # mirror's current's movements one ring outward

ring = 3
side = 2
middle = side // 2

next_corner = 3


while vals[current] <= src:
    # distribute vals[current] to all neighbors with greater indices

    # next immediate neighbor
    addto(vals, current + 1, vals[current])

    if current + 1 == next_corner and not math.sqrt(next_corner) == ring:
        # we are going to turn a corner next time (not the ring corner)
        # 2 blocks ahead is also adjacent
        addto(vals, current + 2, vals[current])

    # shadow and blocks before and after
    addto(vals, shadow - 1, vals[current])
    addto(vals, shadow, vals[current])
    addto(vals, shadow + 1, vals[current])

    if current == next_corner:
        if math.sqrt(next_corner) == ring:
            # next corner is the end of the ring
            addto(vals, current + 2, vals[current])

            ring += 2
            side += 2

            # shadow moves a little more to accomodate for the jump in rings
            shadow += 2

        else:
            # shadow "wraps" around
            shadow += 2
            addto(vals, shadow, vals[current])
            addto(vals, shadow + 1, vals[current])

        # corners increment
        next_corner += side

    if current - 1 == (ring - 2)**2:
        # we just moved up rings, so the blocks below us that are normally
        # less than are actually greater
        addto(vals, shadow - 3, vals[current])
        addto(vals, shadow - 2, vals[current])

    vals.pop(current)
    current += 1
    shadow += 1

print(vals[current])
