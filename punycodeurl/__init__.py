# -*- coding:utf-8 -*-

import absolute_import
import sys

if sys.version_info[0] == 2:
    from .punycodeurl2 import *
elif sys.version_info[0] >= 3:
    from .punycodeurl3 import *
else:
    print("Check your Python version.")
    pass
