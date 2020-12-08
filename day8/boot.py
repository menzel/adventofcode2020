#!/usr/bin/env python3

instructions = []

with open("input") as fp:
    for line in fp:
        instructions.append(line.split())

acc = 0
in_p = 0

known = set()


while True:
    instr = instructions[in_p]

    if in_p in known:
        break
    else:
        known.add(in_p)

    if "jmp" in instr[0]:
        in_p += int(instr[1])
    else:
        if "acc" in instr[0]:
            acc += int(instr[1])
        in_p += 1

print(acc)
