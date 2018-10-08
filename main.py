#! /usr/bin/env python3

import sys
import mylogging

mylogging.init()
logger = mylogging.getLogger(__name__)

if __name__ == '__main__':
    appname = sys.argv[0]
    logger.warning("Starting {} ...".format(appname))
    logger.warning("Finish {}".format(appname))
