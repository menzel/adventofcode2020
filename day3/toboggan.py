#!/usr/bin/env python3

area = []

with open("input") as fp:
    for line in fp:
        area.append(list(line))


pos = [0,0] # row, col

result = 1

slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)] # (down, right)


for slope in slopes:

    counter = 0
    pos = [0,0] # row, col
    while pos[0] < len(area)-1:
        pos[0] += slope[0]
        pos[1] = (pos[1] + slope[1]) % (len(area[0])-1)

        if area[pos[0]][pos[1]] == "#":
            counter += 1

    result *= counter


print(result)
