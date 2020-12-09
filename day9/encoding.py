#!/usr/bin/env python3


n_preamble = 25
pre = []


with open("input") as fp:
    for i,line in enumerate(fp):

        if i < n_preamble:
            pre.append(int(line))
        else:
            if not any([int(line) - p in pre for p in pre]):
                print(line,end="")
                break

            pre.append(int(line))
            pre = pre[1:]

