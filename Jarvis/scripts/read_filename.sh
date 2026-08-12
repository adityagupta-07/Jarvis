#!/bin/bash

# echo > "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/filename.txt"

read -p "Enter the name of the file or folder you want to delete, starting with: " file_nam
file_name="${file_nam,,}"

echo "${file_name}" > "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/filename.txt"

