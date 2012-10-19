#!/usr/bin/env bash
# Permissions : chmod +x fileName.sh
# To launch   : source fileName.sh   OR    ./python.sh
# Definition  : Simple for loop

# Define function here
function bashFunction()
{
    printf "Hellow World\n"
}

# Call function here
for (( i=0; i<5; i++))
do
    bashFunction
done