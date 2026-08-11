#!/bin/bash
result=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "$1*")
count=$(echo "$result" | wc -l)
echo "$count result/s found to delete one by one"

counter=0 
while read -r item <&3; do # read means "read until \n." and store that in item variable 
    # read -p "$(basename "$item") should be deleted? (yes/no): " answer
    echo -n "$(basename "$item") should be deleted? (yes/no): "
    read answer
    if [ "$answer" == "yes" ]; then 
        counter=$((counter + 1))
        rm -rf "$item"
        echo "Deleted: $(basename "$item")" 
    elif [ "$answer" == "no" ]; then
        echo "Skipped: $(basename "$item")"
    elif [ "$answer" == "stop" ]; then
        echo "Deletion stopped"
        break
    else
        echo "Command Unclear. Deletion stopped"
        break
    fi
done 3<<< "$result" 


remaining=$((count - counter))
echo "$counter result/s deleted"
echo "Remaining result/s: $remaining"

# "$result" is data source for this while loop code block
# passing "$result" value as stdin to while code block as cat <<< hi and <<< means literal string/variable whereas < is also used but < means a file
# 3 means fd 3 which is declaration of input source. As we are taking 2 inputs inside this block, one for while loop and another (yes/no) from fd 0 (keyboard stdin). So we need to separate the channel for sources to get input
# < input redirection and used for assigning files
# <<< is here-string and used for assigning literal strings/variables



