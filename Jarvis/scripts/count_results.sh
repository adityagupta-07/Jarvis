#!/bin/bash
   count=$(find ~/.local/share/Trash/files/ -maxdepth 1 -iname "$1*" | wc -l)
   echo "Found $count results"
