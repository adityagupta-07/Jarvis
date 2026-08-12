#!/bin/bash


result=$(cat "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/found_files.txt")

count=0
if [ "$result" != "" ]; then 
    while read -r item; do
        rm -rf "$item"
        count=$((count+1))
    done <<< "$result"
fi

echo "${count}" > "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/count_of_diog.txt"