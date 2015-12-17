# -*- coding: utf-8 -*-
import os
from cf2_measure import Cf2

#print cf2_measure("48003.cf2")

path = "\\\\nasd67f4b\\Cortantes"
path_cf2 = []
for item in os.listdir(path):
    if item.endswith(".cf2"):
        path_cf2.append(item)
for item in path_cf2:
    cutter = Cf2(str(item[:-4]))
    print cutter
    #print cutter.cutter[:-4],">",
    #print cutter.measures()


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #TODO sorted cutter list
    #TODO user can manually insert directory (--dir)
    #TODO user can search for only one cutter (-c)
    #TODO settings file to put default firectory
    #TODO possibility to export to a csv file
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!