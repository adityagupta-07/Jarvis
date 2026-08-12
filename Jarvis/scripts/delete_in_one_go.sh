#!/bin/bash

result=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "$1*")
count=$(echo "$result" | wc -l)
echo -n "Delete $count result/s in one go ? (yes/no): "
read answer

if [ "$answer" == "yes" ]; then 
    while read -r item; do
        rm -rf "$item"
    done <<< "$result"
    echo "$count result/s deleted"
elif [ "$answer" == "no" ]; then 
    echo "Deletion stopped"
else
    echo "Command Unclear. Deletion stopped"
fi
 
 