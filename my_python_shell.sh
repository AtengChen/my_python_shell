#!/bin/bash -e
CURRDIR=$(pwd)
cd $CURRDIR
python . "$*"
