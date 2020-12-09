#!/usr/bin/env python3

with open("input") as fp:
    print(sum([1 for l in fp if (l.split(": ")[1][int(l.split(": ")[0].split()[0].split("-")[0])-1] == l.split(": ")[0].split()[1]) ^ (l.split(": ")[1][int(l.split(": ")[0].split()[0].split("-")[1])-1] == l.split(": ")[0].split()[1])]))
