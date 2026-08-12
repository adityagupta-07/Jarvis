#!/bin/bash

# This script contains both the ways of deletion. (In one go and one by one).
read -p "Enter the name of the file or folder you want to delete, starting with: " file_name # will use terminal to enter file name
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
echo "Found $count result/s." # Output from Jarvis 

if [ "$count" != 0 ]; then 

    read -p "Shall $count result/s be deleted? (yes/no): " answer # Output from Jarvis and it should accept the voice command (yes/no)

    if [ "$answer" == "yes" ]; then
        read -p "How the result/s should get deleted? 
        (In one go: 1)
        (One by one: 2) 
        Please choose (1/2): " way_of_deletion # Output from jarvis and should accept voice command (one/two)

        if [ "$way_of_deletion" == "1" ]; then # will compare with voice == "one"
            read -p "Delete $count result/s in one go? (yes/no): " ans1 # Output from Jarvis and it should accept the voice command (yes/no)

            if [ "$ans1" == "yes" ]; then 
                count_of_in_one_go=0
                while read -r item; do
                    rm -rf "$item"
                    count_of_in_one_go=$((count_of_in_one_go + 1))
                done <<< "$result"
                echo "$count_of_in_one_go result/s deleted." #Output from jarvis
            elif [ "$ans1" == "no" ]; then
                echo "Deletion stopped" #Output from jarvis
            else
                echo "Command Unclear. Deletion stopped" #Output from jarvis
            fi
        elif [ "$way_of_deletion" == "2" ]; then # will compare voice == "two"
            echo "$count result/s found to delete one by one." #Output from jarvis
            count_of_one_by_one=0 
            while read -r item <&3; do  
                read -p "$(basename "$item") should be deleted? (yes/no): " ans2 # Output from Jarvis and it should accept the voice command (yes/no)
                if [ "$ans2" == "yes" ]; then 
                    rm -rf "$item"
                    count_of_one_by_one=$((count_of_one_by_one + 1))
                    echo "Deleted: $(basename "$item")" #Output from jarvis
                elif [ "$ans2" == "no" ]; then
                    echo "Skipped: $(basename "$item")" #Output from jarvis
                elif [ "$ans2" == "stop" ]; then
                    echo "Deletion stopped" #Output from jarvis
                    break
                else
                    echo "Command unclear. Deletion stopped." #Output from jarvis
                    break
                fi
            done 3<<< "$result" 

            remaining=$((count - count_of_one_by_one))
            echo "$count_of_one_by_one result/s deleted" #Output from jarvis
            echo "Remaining result/s: $remaining" #Output from jarvis

        else
            echo "Deletion stopped." #Output from jarvis
        fi
    elif [ "$answer" == "no" ]; then
        echo "Deletion stopped." #Output from jarvis
    else
        echo "Command unclear. Deletion stopped." #Output from jarvis
    fi
fi