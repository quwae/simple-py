#! /usr/bin/env python3

import logging

def init(filename='logfile.txt',level=logging.DEBUG):
    logging.basicConfig(filename=filename,level=level,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')

def getLogger(name):
    return logging.getLogger(name)

