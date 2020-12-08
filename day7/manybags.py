#!/usr/bin/env python3

import re
graph = {}

with open("input") as fp:
    for line in fp:
        match = re.match("((\w+\s)+)contain\s((no other)|.*)\.", line)

        parent = re.sub("(\d\s)|(bags?)|(\s)", "",match.group(1))
        children = [re.sub("(bags?)|(\s)", "",m) for m in match.group(3).split(", ")]

        if not parent in graph:
            graph[parent] = []
        if not "noother" in children:
            graph[parent] += children

outer = ["1shinygold"]

# iterate over bags in outer
for i,val in enumerate(outer):

    # evaluate those with a number at beginning, ignore others
    if re.match("\d.*",val): 

        outer += [val[1:]] * (int(val[0])-1)  # add number of bags of current color, without number at beginning
        outer += (list(graph[val[1:]])) * int(val[0]) # add children of current color, with number to eval again 
        outer[i] = val[1:] # remove number from color name

print(len(outer)-1) # sub 1 b/c first shinygold bag is still in the outer list
