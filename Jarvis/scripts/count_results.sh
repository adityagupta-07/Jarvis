#!/bin/bash

# Option 1:
# count=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "$1*" | wc -l)
# echo "Found $count result/s"
 
# Option 2
read -p "Enter the name of the file or folder you want to delete, starting with: " file_name
file_name_lower="${file_name,,}"

result=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "${file_name_lower}*")
if [ "$result" == "" ]; then 
   # If find matches nothing, result="" (truly empty, no \n).
   # But echo always appends its own \n, even to an empty string 
   # so echo "$result" emits a single \n as result="" and has nothing to print
   # wc -l just counts \n characters in its input, so it sees that one \n
   # and reports 1, even though 0 files were actually found.
   count=0
else
   count=$(echo "$result" | wc -l)
fi
echo "Found $count result/s."