# Advent of Code, Day 3, Part a
# Lee Cattarin

import math

src = 265149

prev = 1
i = 1
while True:
    corner = i**2
    if src > corner:
        prev = corner
        i += 2
        continue

    if src <= corner:
        side = (corner - prev) // 4
        print("corner:", corner, "prev corner:", prev, "side:", side)

        # find the corner immediately after the src
        while src <= corner - side:
            corner = corner - side
            print("closer corner:", corner)

        inward_dist = i // 2

        middle = corner - (side // 2)
        print("middle:", middle)
        lateral_dist = abs(middle - src)

        print(inward_dist, lateral_dist)
        print(inward_dist + lateral_dist)
        break
