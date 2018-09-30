#! /usr/bin/env python3

import sys
import logging

if __name__ == '__main__':
    appname = sys.argv[0]
    logging.warning("Starting {} ...".format(appname))
    logging.warning("Finish {}".format(appname))
