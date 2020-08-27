#!/bin/bash

if [ $# -eq 0 ]; then
    echo "gen-svg: Please spcify a dot file"
    exit 1
fi

neato -n2 -Tsvg "$1" -o cur.svg
