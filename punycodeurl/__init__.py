# -*- coding:utf-8 -*-

import sys

if sys.version_info[0] == 2:
    from punycodeurl2 import *
elif sys.version_info[0] >= 3:
    from punycodeurl3 import *
else:
    print("The twentieth century called, it wants its code back.")
    pass
