#! /bin/bash
echo -n "*** Please type filename to put copied to lxplus: "
read -e FILENAME
echo -n "*** scp "$FILENAME" attikis@lxplus.cern.ch:/afs/cern.ch/user/a/attikis/public/html/attikis/docs/./"
echo
scp $FILENAME attikis@lxplus.cern.ch:/afs/cern.ch/user/a/attikis/public/html/attikis/docs/.
