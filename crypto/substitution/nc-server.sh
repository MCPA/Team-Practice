#!/bin/sh
# Note that the results from this may not be what you wanted ... check the simple server as well.

if [ $# -lt 2 ]
  then
    echo "Not enough arguments supplied"
    echo "Usage: ./nc-server.sh <binary> <port>"
else
  while true; do nc -l -p $2 -e ./$1 ; done
fi
