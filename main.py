#! /usr/bin/env python3

import sys
import logger

if __name__ == '__main__':
    appname = sys.argv[0]
    logger.init()
    logger.warning("Starting {} ...".format(appname))
    logger.warning("Finish {}".format(appname))
