import subprocess
import time

# subprocess.Popen(["gnome-terminal", "--", "bash", "-c", "./scripts/deletion_script.sh; exec bash"])
subprocess.Popen(["gnome-terminal", "--", "bash", "-c", "./scripts/deletion_script.sh; sleep 1"])

count = 0
while True:
    count = count + 1
    print(f"[python] tick {count}")
    time.sleep(1)


