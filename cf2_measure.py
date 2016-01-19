# -*- coding: utf-8 -*-
from re import split
import options
import os

class Cf2(object):
    ext = ".cf2"
    def __init__(self, cutter):
        self.cutter = cutter

        while str(self.cutter).endswith(".cf2"):
            #pass
            self.cutter = self.cutter[:-4]
        else:
            path = options.opt_dir()
            if not (path.endswith('/') or path.endswith('\\')):
                path = path + '/'
            #dir_list = []
            #dir_list.append(path)
            #dir_list.append(self.cutter)
            #dir_list.append(self.ext)
            #dir = ''.join(dir_list)
            #print type(path)
            #dir = path + str(self.cutter) + self.ext
            dir = os.path.join(path, (self.cutter).decode('utf8') + (self.ext).decode('utf8'))
            f = open(dir, 'r')
            file_contents = f.read()
            f.close()
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
                self.width = UR1
            if abs(LL2) == 0:
                self.height = UR2
            if LL1 < 0:
                if UR1 > LL1:
                    self.width = abs(LL1) + abs(UR1)
                    self.width -= 1
            if LL1 > 0:
                if UR1 > LL1:
                    self.width = UR1 - LL1
            if LL2 < 0:
                if UR2 > LL2:
                    self.height = abs(LL2) + abs(UR2)
                    self.height -= 1
            if LL2 > 0:
                if UR2 > LL2:
                    self.height = UR2 - LL2
            if self.width == 0 or self.height == 0:
                return "ERROR, 0"
    def __repr__(self):
        #return ("{:s}.cf2 > {:s}\nCutter: {:s}\nMeasures: {:s}\nWidth: {:d}\nHeight: {:d}".format(self.cutter, self.measures(), self.cutter, self.measures(), self.width, self.height))
        #return "".join((cutter,".cf2 > ",measures,"\nCutter: ",cutter,"\nMeasures: ",measures,"\nWidth: ",str(width),"\nHeight: ",str(height)))
        return ("{:s}.cf2 > {:s}".format(self.cutter, self.measures()))
    def measures(self):
        return str(self.width) + 'x' + str(self.height)
    def _width(self):
        return self.width
    def _height(self):
        return self.height
    def _cutter(self):
        if str(self.cutter).endswith(".cf2"):
            return self.cutter[:-4]
        else:
            return self.cutter

#cutter = Cf2("18986")
#print cutter