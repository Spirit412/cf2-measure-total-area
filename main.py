# -*- coding: utf-8 -*-
import os

import options
from options import parser
from cf2_measure import Cf2

def list_cf2(cf2):
    path = options.opt_dir()
    if not (path.endswith('/') or path.endswith('\\')):
        path = path + '/'
    path_cf2 = []
    #print os.listdir(path)
    if cf2 == "*":
        for item in os.listdir(path):
            if item.endswith(".cf2"):
                path_cf2.append(item)
        for item in path_cf2:
            cutter = Cf2(item)
            print cutter
    else:
        cutter = Cf2(cf2)
        print cutter

def main():
    args = parser.parse_args()
    argPath = args._argPath
    list_cf2(argPath)

if __name__ == '__main__':
    main()

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #TODO sorted cutter list
    #TODO user can manually insert directory (--dir)
    #TODO user can search for only one cutter (-c)
    #TODO settings file to put default directory
    #TODO possibility to export to a csv file
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!