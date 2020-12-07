#!/usr/bin/env python3

def find(s,high,low,lower_char):
    diff = high - low

    if diff == 1:
        if s[0] == lower_char: # take lower 
            return low
        else: # take lower
            return high
    else:
        if s[0] == lower_char: # take lower 
            high -= 1+diff//2
        else: # take higher
            low += 1+diff//2
        return find(s[1:],high,low,lower_char)


def seat(string):
    rows = string[:7]
    seats = string[7:]

    row = find(rows,127,0,"F")
    seat = find(seats,7,0,"L")

    return row * 8 + seat

with open("input") as fp:
    print((set(range(70,826)) - set([seat(line) for line in fp])).pop())
