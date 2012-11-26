#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Enable tab-completion in interactive default Python shell. NOT Executable.

# Launch python shell and import the following
python
import rlcompleter, readline
readline.parse_and_bind('tab: complete')
