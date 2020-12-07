#!/usr/bin/env python3

import re

valids = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

counter = 0


def checkpp(pp):
    if len(valids & pp.keys()) != 8:
        return False

    if not 1920 <= int(pp["byr"]) <= 2002:
        return False
    if not 2010 <= int(pp["iyr"]) <= 2020:
        return False
    if not 2020 <= int(pp["eyr"]) <= 2030:
        return False
    if not "cm" in pp["hgt"] and not "in" in pp["hgt"]:
        return False
    if "cm" in pp["hgt"]:
        if not 150 <= int(pp["hgt"].replace("cm", "")) <= 193:
            return False
    if "in" in pp["hgt"]:
        if not 59 <= int(pp["hgt"].replace("in", "")) <= 76:
            return False
    if not re.match("^#[0-9a-f]{6}$", pp["hcl"]):
        return False
    if not pp["ecl"] in "amb blu brn gry grn hzl oth".split():
        return False
    if not re.match("^\d{9}$", pp["pid"]):
        return False

    return True


with open("input") as fp:
    pp = {"cid": ""}

    for line in fp:
        if len(line) > 1:
            pp.update({e.split(":")[0]: e.split(":")[1] for e in line.split()})
        else:

            if checkpp(pp):
                counter += 1
            pp = {"cid": ""}

if checkpp(pp):
    counter += 1

print(counter)
