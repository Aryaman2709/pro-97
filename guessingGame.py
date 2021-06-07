import random


number = random.randint(1, 9)
chances = 0

while chances < 5:
    guess = int(input("Enter your guess: "))
    if(guess > number):
        print("Incorrect! The number is too great")
    elif(guess < number):
        print("Incorrect! The number is too low")
    elif(guess == number):
        print("Congratulations! You Won!")
    chances = chances +1

if not chances<5:
    print("Games Up!")
    