#! /usr/bin/env python3

import logging

def init(filename='logfile.txt',level=logging.DEBUG):
    logging.basicConfig(filename=filename,level=level,format='%(asctime)s %(message)s')

def debug(msg):
    logging.debug(msg)

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def error(msg):
    logging.error(msg)

def critical(msg):
    logging.critical(msg)

