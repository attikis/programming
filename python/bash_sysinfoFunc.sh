#!/usr/bin/env bash
# Permissions : chmod +x fileName.sh
# To launch   : source fileName.sh   OR    ./python.sh
# Definition  : 

# Define functions here
function uname_func ()
{
    UNAME="uname -a"
    printf "+++ Gathering system information with the $UNAME command: \n\n"
    $UNAME
}

function disk_func ()
{
    DISKSPACE="df -h"
    printf "+++ Gathering system information with the $DISKSPACE command: \n\n"    
    $DISKSPACE
}

function main ()
{
    uname_func
    disk_func
}

main