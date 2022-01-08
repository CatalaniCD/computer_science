#!/bin/bash
# Check the file system using a recursive tree search
# pre-order : Node-Left-Right
# in-order  : Left-Node-Right
# post-order: Left-Right-Node
# keep Left & right in same order
# arrange node as identity matrix

listR() # Case of in-order recursion : start on a, a1, a11, a111, a12, a13, a121, 
{
        cd $1
        echo -e "\n Directory : $1"
        ls --color=auto
        list=`ls`
        for file in $list
        do
                if [ -d $file ]
                then
                        listR $file
                        cd ..
                fi
        done
}

listR .

