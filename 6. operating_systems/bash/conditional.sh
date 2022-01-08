#!/bin/bash
read name
if [ -d $name ]
then
    cd $name
    touch helloworld.cpp
    echo "File created"
else
    echo "$name is not a directory"
fi
