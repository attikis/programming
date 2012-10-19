#!/usr/bin/perl
#To launch: perl fileName.pl

if (-d "/tmp") {
    print "/tmp is a directory\n";
}
else {
    print "/tmp is not a directory\n";
}
