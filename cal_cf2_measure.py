# -*- coding: utf-8 -*-
from re import split

def cf2_measure(cf2):
    cf2 = str(cf2)
    dir = '\\\\nasd67f4b\\Cortantes\\' + cf2
    f = open(dir, 'r')
    file_contents = f.read()
    width = 0
    height = 0

    for line in file_contents.splitlines():
        #Atribuição de UR1 e UR2
        if line.startswith('UR,'):
            UR1,UR2 = ''.join(line.split(',')[1]),''.join(line.split(',')[2])
            UR1,UR2 = round(float(UR1)),round(float(UR2))
            UR1,UR2 = int(UR1),int(UR2)
        #Atribuição de LL1 e LL2
        elif line.startswith('LL,'):
            LL1,LL2 = ''.join(line.split(',')[1]),''.join(line.split(',')[2])
            LL1,LL2 = round(float(LL1)),round(float(LL2))
            LL1,LL2 = int(LL1),int(LL2)

    if abs(LL1) == 0:
        width = UR1
    if abs(LL2) == 0:
        height = UR2
    if LL1 < 0:
        if UR1 > LL1:
            width = abs(LL1) + abs(UR1)
            width -= 1
    if LL1 > 0:
        if UR1 > LL1:
            width = UR1 - LL1
    if LL2 < 0:
        if UR2 > LL2:
            height = abs(LL2) + abs(UR2)
            height -= 1
    if LL2 > 0:
        if UR2 > LL2:
            height = UR2 - LL2
    f.close()
    if width == 0 or height == 0:
        return "ERROR, 0"
    else:
        return str(width) + 'x' + str(height)