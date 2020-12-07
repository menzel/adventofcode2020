#!/usr/bin/env python3


with open("input") as fp:

    answers = set([chr(i) for i in range(ord('a'),ord('z')+1)])
    result = 0

    for line in fp:
        if len(line) <= 1:
            result += (len(answers))
            answers = set([chr(i) for i in range(ord('a'),ord('z')+1)])
        else:
            answers = answers & (set(list(line.rstrip())))

result += (len(answers))
print(result)
