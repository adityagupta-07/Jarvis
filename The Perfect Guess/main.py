import random

n = random.randint(1, 101) # 1 to 100
guesses = 0
a = 0 # declaration of a just to enter the loop

while (a != n):
    a = int(input("Guess a number: "))
    guesses += 1
    if (a < n):
        print("Higher number please")
    else: 
        print("Lower number please")

if (a == n):
    print(f"You guessed {n} in {guesses} attempts.")
else:
    print("Something went wrong.")