# -*- coding: utf-8 -*-
import argparse
import configparser

#Get directory from config.ini
def opt_dir():
    #global path
    config = configparser.RawConfigParser()
    #config.read('config.ini')
    config.read_file(open('config.ini'))
    if config.get('SETTINGS', 'dir', raw=True) == "":
        return "ERROR DIR NOT MENTIONED"
    else:
        path = config.get('SETTINGS', 'dir', raw=True)
        path = path.encode()
        return path


parser = argparse.ArgumentParser(description='A script to measure the total area of a single or multiple .cf2 file/s')

parser.add_argument('-c', required=False, metavar='CUTTER', dest='_argPath',
                   help='specify the cutter. required argument. to change the folder of your cutter change it inside config.ini file')

def main():
    args = parser.parse_args()

if __name__ == '__main__':
    main()