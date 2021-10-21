#Will start witing the code soon, that will handle Exceptions!

import random

print("Welcome to this Game!\nYou need to Guess a number between 0 and 100 ")
randomnum = random.randint(0,100)
i = 1
name = input("Enter Your Name : ")
guessednum = int(input("Enter your first Guess : "))
while(guessednum!=randomnum):
    i += 1
    if(guessednum>randomnum):
        print("Your guess is not correct!\n Guess a Smaller number then you guessed previously.")
    if(guessednum<randomnum):
        print("Your guess is not correct!\n Guess a Larger number then you guessed previously.")
            
    guessednum =  int(input("Enter your next Guess : "))

print("Congratulations! Your Guess is correct.")
print(f"You guessed the number in {i} times.")
with open("highscore.txt") as f:
    text = f.read()
    text = text.split()

if(int(text[1])>i):
    print(f'''Congratulations! You Just broke the HighScore made by "{text[0]}"''')
    with open("highscore.txt", "w") as f:
        f.write(f"{name} - {str(i)}")