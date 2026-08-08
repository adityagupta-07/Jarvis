import random

# 1 for snake
# -1 for water 
# 0 for gun

computer = random.choice([1, -1, 0])
youstr = input("Enter you choice (s/w/g): ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]
reversedDict = {1: "Snake", -1: "water", 0: "gun"}

print(f"You chose {reversedDict[you]} \nComputer chose {reversedDict[computer]}")

if (computer == you):
    print("Its a draw")
# elif (computer == 1 and you == -1): #(computer - you) = 2
#     print("You lose")
# elif (computer == 1 and you == 0): #(computer - you) = 1
#     print("You win")
# elif (computer == -1 and you == 1): #(computer - you) = -2
#     print("You win")
# elif (computer == -1 and you == 0): #(computer - you) = -1
#     print("You lose")
# elif (computer == 0 and you == 1): #(computer - you) = -1
#     print("You lose")
# elif (computer == 0 and you == -1): #(computer - you) = 1
#     print("You win")
elif ((computer - you == 2) or (computer - you == -1)):
    print("You lose")
else: 
    print("You win")
# else:
#     print("Something went wrong")