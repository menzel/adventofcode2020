#!/usr/bin/env python3

counter = 0

with open("input") as fp:
    for line in fp:
        parts = line.split(": ")

        rule = parts[0].split()
        rng = rule[0].split("-")
        pw = parts[1]

        if (pw[int(rng[0])-1] == rule[1]) ^ (pw[int(rng[1])-1] == rule[1]):
            counter += 1

print(counter)
