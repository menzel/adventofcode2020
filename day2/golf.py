#!/usr/bin/env python3

with open("input") as fp:
    print(sum([1 for line in fp if (line.split(": ")[1][int(line.split(": ")[0].split()[0].split("-")[0])-1] == line.split(": ")[0].split()[1]) ^ (line.split(": ")[1][int(line.split(": ")[0].split()[0].split("-")[1])-1] == line.split(": ")[0].split()[1])]))
