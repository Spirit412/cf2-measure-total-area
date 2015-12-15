# -*- coding: utf-8 -*-
import os
from cal_cf2_measure import cf2_measure

#print cf2_measure("48003.cf2")

path = "\\\\nasd67f4b\\Cortantes"
path_cf2 = []
for item in os.listdir(path):
    if item.endswith(".cf2"):
        path_cf2.append(item)
for item in path_cf2:
    print item[:-4],">",
    print cf2_measure(item)