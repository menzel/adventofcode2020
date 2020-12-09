#!/usr/bin/env python3


n_preamble = 25
pre = []
all_numbers  = []

import itertools

def find_weakness(number, numbers):

    #iterate over each permutation of the available numbers
    for p in itertools.permutations(numbers):
        # iterate over each possible start and end value for sub lists

        for start in range(0,len(all_numbers)-1): 
            for end in range(start+1,len(all_numbers)):

                # if this sub list adds up to the correct number print and return
                if sum(p[start:end]) == number:
                    #print(p[start:end])
                    print(max(p[start:end]) + min(p[start:end]))
                    return


with open("input") as fp:
    for i,line in enumerate(fp):
        all_numbers.append(int(line))

        if i < n_preamble: # only add numbers for the first n numbers
            pre.append(int(line)) 
        else:
            if not any([int(line) - p in pre for p in pre]):

                # found number from first challenge, then find weakness:
                find_weakness(int(line),all_numbers)
                break

            pre.append(int(line))
            pre = pre[1:]
