#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

import math

# the x magic number is between 6444429920 and 6444429921
def e():
        x = 6444429920 + 0.22 # or int(0x1801e3260,16) + 0.22
        ret = (1+(1.0/x))**x
        return ret

print math.e
print e()
