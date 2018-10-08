#! /usr/bin/env python3

import sys
import mylogging

if __name__ == '__main__':
    appname = sys.argv[0]
    mylogging.init()
    mylogging.warning("Starting {} ...".format(appname))
    mylogging.warning("Finish {}".format(appname))
