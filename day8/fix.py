#!/usr/bin/env python3

instructions = []

with open("input") as fp:
    for line in fp:
        instructions.append(line.split())


orig = tuple(instructions)

for i,n in enumerate(orig): #iterate over each instruction

    instructions = list(orig)
    known = set()

    acc = 0
    in_p = 0

    # change instruction if nop or jmp 
    if "jmp" in n:
        instructions[i] = ["nop ", n[1]]
    elif "nop" in n:
        instructions[i] = ["jmp ", n[1]]
    else: # for acc:
        continue 

    # evaluate program like before
    while True:
        instr = instructions[in_p]

        if in_p in known:
            breakA # loop detected, abort
        else:
            known.add(in_p)

        if "jmp" in instr[0]:
            in_p += int(instr[1])
        else:
            if "acc" in instr[0]:
                acc += int(instr[1])
            in_p += 1
        
        # program has finished
        if in_p == len(orig):
            print(acc)
            break

    # finished program fount, break for loop
    if in_p == len(orig):
        break
