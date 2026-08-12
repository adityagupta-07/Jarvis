#!/bin/bash

result=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "$1*")
count=$(echo "$result" | wc -l)

if [ "$result" == "" ]; then 
    # If find matches nothing, result="" (truly empty, no \n).
    # But echo always appends its own \n, even to an empty string 
    # so echo "$result" emits a single \n as result="" and has nothing to print
    # wc -l just counts \n characters in its input, so it sees that one \n
    # and reports 1, even though 0 files were actually found.
    count=0    
fi

echo "${result}" > "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/found_files.txt"
echo "${count}" > "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/count.txt"


