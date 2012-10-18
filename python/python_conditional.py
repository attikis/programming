#!/usr/bin/env python
#To launch: python fileName.py

import os

if os.path.isdir("/tmp"):
    print "/tmp is a directory"
else:
    print "/tmp is not a directory"
