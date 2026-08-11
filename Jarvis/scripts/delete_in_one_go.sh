#!/bin/bash

result=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "$1*")
count=$(echo "$result" | wc -l)
echo "$count result/s found to delete in one go"

while read -r item; do
    rm -rf "$item"
done <<< "$result"

echo "$count result/s deleted"