#!/usr/bin/env python3

import sys

values = set()

with open("input") as fp:
    for line in fp:
        values.add(int(line))

for val in values:
    for val2 in values:
        if (2020 - val - val2) in values:
            print(val*(2020-val - val2) * val2)

