#!/usr/bin/env python3

import sys

values = set()

with open("input") as fp:
    for line in fp:
        values.add(int(line))

for val in values:
    if (2020 - val) in values:
        print(val)
        print(2020-val)
        print(val*(2020-val))

