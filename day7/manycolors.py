#!/usr/bin/env python3

import re
graph = {}


with open("input") as fp:
    for line in fp:
        match = re.match("((\w+\s)+)contain\s((no other)|.*)\.", line)

        parent = re.sub("(\d\s)|(bags?)|(\s)", "",match.group(1))
        children = [re.sub("(\d\s)|(bags?)|(\s)", "",m) for m in match.group(3).split(", ")]

        if not parent in graph:
            graph[parent] = []
        if not "noother" in children:
            graph[parent] += children

outer = {"shinygold"}
lastlenouter = 0


# iterate until no more change:
while lastlenouter != len(outer):

    # update len for loop 
    lastlenouter = len(outer)

    # tmp store children colors
    tmp = set()

    for key in outer: # iterate over known outer colors
        for color in graph.keys(): # iterate over graph 
            if key in graph[color]: # if the current outer color is in the graphs children, add parent to known outer (over tmp list)
                tmp.add(color)
    outer = outer | tmp

print(len(outer)-1) # sub 1 b/c outer still contains shinygold init 
