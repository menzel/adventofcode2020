#!/usr/bin/env python3

valids = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

counter = 0

with open("input") as fp:

    keys = set()

    for line in fp:
        if len(line) > 1:
            keys = keys.union(set([x.split(":")[0] for x in line.split( )]))
        else:
            keys.add("cid")
            if len(valids & keys) == 8:
                counter += 1
            keys = set()

print(counter)


