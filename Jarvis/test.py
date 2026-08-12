file_path = "/home/aditya/Coding/Python Porjects - YT -CWH/Python-Mini-Projects/Jarvis/tmp/found_files.txt"

with open(file_path, "r") as f:
    lines = f.readlines()
    print(lines[0])

count = len(lines)
print(count)