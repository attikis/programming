#!/usr/bin/env bash
# Permissions : chmod +x fileName.sh
# To launch   : source fileName.py    OR    ./fileName.sh
# Definition  : Prints system information

# Command 1 (Leace no blank space in declarations!)
UNAME="uname -a"
printf "+++ Gathering system information with $UNAME command:\n\n"
$UNAME

# Command 2
DISKSPACE="df -h"
printf "+++ Gathering system information with $DISKSPACE command:\n\n"
$DISKSPACE

