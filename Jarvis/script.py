import subprocess
 
keyword = input("Enter the file or folder name starting with: ").strip().lower()
result = subprocess.run(["./scripts/count_results.sh", keyword])

answer = input("Shall the result/s be deleted? (yes/no): ").strip().lower()

if answer == "yes":
    one_go_or_not = input("How the result/s should get deleted? \n (In one go: 1) \n (One by one: 2) \n Please choose (1/2): ").strip().lower()
    if one_go_or_not == "1":
        delete_in_one_go = subprocess.run(["./scripts/delete_in_one_go.sh", keyword])
    elif one_go_or_not == "2":
        delete_one_by_one = subprocess.run(["./scripts/delete_one_by_one.sh", keyword])
    else:
        print("Deletion stopped.")
else:
    print("Deletion stopped.")






