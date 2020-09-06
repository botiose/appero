#!/bin/bash

if [ $# -eq 1 ]; then
    neato -n2 -Tpng "$1" -o out.png
else
    count=0
    for dir in $(ls | grep 0); do
        for file in $(ls "$dir"); do
            nid="$count"
            if [ $count -lt 10 ]; then
                nid="0$count"
            fi
            neato -n2 -Tpng "$dir/$file" -o images/$nid-graph.png
            
            count=$((count+1))
        done
    done
fi


